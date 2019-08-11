# -*- coding: utf-8 -*-
import datetime
import hashlib
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
from ...settings import *


class Executor(ThreadPoolExecutor):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, "_instance", None):
            cls._instance = ThreadPoolExecutor(max_workers=10)
        return cls._instance


class Http(Service):

    handler = None

    def set_handler(self, handler):
        self.handler = handler
        return self

    def listen(self, port, addr='0.0.0.0'):
        self.port = port
        self.addr = addr
        return self

    def _start(self):
        app = tornado.web.Application(handlers=[
            (r'/cs', Http.BaseHandler, dict(handler=self.handler)),
            (r'/wx', Http.WeixinHandler, dict(handler=self.handler))
        ])
        http_server = tornado.httpserver.HTTPServer(app)
        http_server.listen(self.port, address=self.addr)
        logging.info(f'Tornado:listen:{self.addr}:{self.port}')
        tornado.ioloop.IOLoop.instance().start()

    def _stop(self):
        pass

    class BaseHandler(tornado.web.RequestHandler):

        executor = Executor()
        handler = None

        def initialize(self, handler):
            self.handler = handler

        @tornado.gen.coroutine
        def get(self):
            uid = self.get_argument('uid')
            q = self.get_argument('q')
            logging.info(f'HttpHandler:uid={uid},q={q}')
            # -> not functioning now
            # future = self.executor.submit(self.answer, uid, q)
            # response = yield tornado.gen.with_timeout(datetime.timedelta(10), future,
            #                                           quiet_exceptions=tornado.gen.TimeoutError)
            # -> missing tornado.gen.Task
            # response = yield tornado.gen.Task(self.answer, uid, q)
            response = yield self.answer(uid, q)
            if response:
                # self.write(response.result())
                self.write(response)

        # @tornado.concurrent.run_on_executor
        @tornado.gen.coroutine
        def answer(self, uid, q):
            if self.handler:
                return self.handler(uid, q)
            else:
                logging.error('HttpHandler:missing handler')

        def data_received(self, chunk):
            pass

    class WeixinHandler(tornado.web.RequestHandler):

        executor = Executor()
        handler = None

        def initialize(self, handler):
            self.handler = handler

        def get(self):
            try:
                signature = self.get_argument("signature")
                timestamp = self.get_argument("timestamp")
                nonce = self.get_argument("nonce")
                echo_str = self.get_argument("echostr")
                if not (signature and timestamp and nonce and echo_str):
                    return "hello, this is handle view"
                token = WECHAT_TOKEN

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

        @tornado.gen.coroutine
        def post(self):
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

        @tornado.concurrent.run_on_executor
        def answer(self, uid, q):
            if self.handler:
                return self.handler(uid, q).replace("<br />", "\n")
            else:
                logging.error('[WeixinHandler] missing handler.')

        def data_received(self, chunk):
            pass
