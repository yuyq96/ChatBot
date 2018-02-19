# ChatBot

Support multiple chatbots, targeted for questions & answers or daily conversation, and multiple API, including http, Wechat and Wechat Mass Platform.

## Bots

### QA

- [elastic](https://github.com/archie-yu/ChatBot/blob/master/chatbot/bot/elastic.py)

  - Based on FQA and tags match, using [Elasticsearch](https://github.com/elastic/elasticsearch) for searching tags.
  
  - Run Elasticsearch before using this bot.

- TODO

### Talk

- [tuling](https://github.com/archie-yu/ChatBot/blob/master/chatbot/bot/tuling.py)

  - Based on [Tuling Robot](http://www.tuling123.com).
  
  - Get your API key from the Tuling Robot [website](http://www.tuling123.com) and set it in the `ChatBot.cfg`.

## API

- [http](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/http.py)

  - Based on [Tornado](https://github.com/tornadoweb/tornado).
  
  - Support Wechat Mass Platform API.

- [wechat](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/wechat.py)

  - Based on [ItChat](https://github.com/littlecodersh/ItChat).
  
  - Got some login problems now.

- [wechatmp](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/wechatmp.py)

  - Based on [ItChatmp](https://github.com/littlecodersh/ItChatmp).
  
  - Get your token, appID, appSecret from the Wechat Mass Platform [website](https://mp.weixin.qq.com/) and set it in the `ChatBot.cfg`.

## Getting Started

### Settings

- Dependencies

  [`Elasticsearch`](https://github.com/elastic/elasticsearch) + [`IK Analysis`](https://github.com/medcl/elasticsearch-analysis-ik), [`Tornado`](https://github.com/tornadoweb/tornado), [`ItChat`](https://github.com/littlecodersh/ItChat), [`ItChatmp`](https://github.com/littlecodersh/ItChatmp)

- Clone project

```
git clone https://github.com/archie-yu/ChatBot.git
```

- Copy [`ChatBot.cfg.template`](https://github.com/archie-yu/ChatBot/blob/master/ChatBot.cfg.template) to `ChatBot.cfg`

```
cd ChatBot
cp ChatBot.cfg.template ChatBot.cfg
```

- Configure `ChatBot.cfg`

### Demo

See [`demo.py`](https://github.com/archie-yu/ChatBot/blob/master/demo.py)

## License

[LGPL-3.0](https://github.com/archie-yu/ChatBot/blob/master/LICENSE)
