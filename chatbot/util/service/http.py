# -*- coding: utf-8 -*-
import datetime
import hashlib
import logging
from concurrent.futures import ThreadPoolExecutor

import tornado.concurrent
import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from . import receive
from . import reply
from .abstract import Service

define("port", default=80, help="Run server on the given port", type=int)


class Executor(ThreadPoolExecutor):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, "_instance", None):
            cls._instance = ThreadPoolExecutor(max_workers=10)
        return cls._instance


class Http(Service):

    def _start(self):
        tornado.options.parse_command_line()
        app = tornado.web.Application(handlers=[
            (r"/", Http.BaseHandler, dict(bot=self.bot)),
            (r"/wx", Http.WeixinHandler, dict(bot=self.bot))
        ])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(options.port)
        logging.info("Running server on port %u", options.port)
        tornado.ioloop.IOLoop.instance().start()

    def _stop(self):
        pass

    class BaseHandler(tornado.web.RequestHandler):

        executor = Executor()
        bot = None

        def initialize(self, bot):
            self.bot = bot

        @tornado.web.asynchronous
        @tornado.gen.coroutine
        def get(self):
            uid = self.get_argument("uid")
            q = self.get_argument("q")
            if q:
                logging.info("[HttpHandler] uid=%s,q=%s" % (uid, q))
                future = self.executor.submit(self.answer, uid, q)
                response = yield tornado.gen.with_timeout(datetime.timedelta(10), future,
                                                          quiet_exceptions=tornado.gen.TimeoutError)
                if response:
                    self.write(response.result())
            else:
                self.write("Missing question.")

        @tornado.concurrent.run_on_executor
        def answer(self, uid, q):
            if self.bot:
                return self.bot.answer(q)
            else:
                return "Bot error."

        def data_received(self, chunk):
            pass

    class WeixinHandler(tornado.web.RequestHandler):

        executor = Executor()
        bot = None

        def initialize(self, bot):
            self.bot = bot

        def get(self):
            try:
                signature = self.get_argument("signature")
                timestamp = self.get_argument("timestamp")
                nonce = self.get_argument("nonce")
                echo_str = self.get_argument("echostr")
                if not (signature and timestamp and nonce and echo_str):
                    return "hello, this is handle view"
                token = TOKEN_WECHAT

                alist = [token.encode("utf-8"), timestamp.encode("utf-8"), nonce.encode("utf-8")]
                alist.sort()
                sha1 = hashlib.sha1()
                tuple(map(sha1.update, alist))
                hashcode = sha1.hexdigest()
                logging.info("handle/GET func: hashcode: %s, signature: %s" % (hashcode, signature))
                if hashcode == signature:
                    self.write(echo_str)
                else:
                    self.write("")
            except Exception as e:
                logging.error(type(e))

        @tornado.web.asynchronous
        @tornado.gen.coroutine
        def post(self):
            # try:
            web_data = self.request.body
            logging.info("Handle Post web data is %s" % web_data)
            recMsg = receive.parse_xml(web_data)
            if isinstance(recMsg, receive.TextMsg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                future = self.executor.submit(self.answer, toUser, recMsg.Content.decode("utf-8"))
                response = yield tornado.gen.with_timeout(datetime.timedelta(10), future,
                                                          quiet_exceptions=tornado.gen.TimeoutError)
                if response:
                    content = response.result()
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                    self.write(replyMsg.send())
            else:
                logging.info("Unknown data")
                self.write("success")
            # except Exception as e:
            #     logging.error(type(e))

        @tornado.concurrent.run_on_executor
        def answer(self, uid, q):
            if self.bot:
                return self.bot.answer(q).replace("<br />", "\n")
            else:
                return "Bot error"

        def data_received(self, chunk):
            pass
