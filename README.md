# ChatBot

Various chatbots, including question & answering type and daily conversation type.

Various platforms, including http, Wechat and Wechat Mass Platform.

## Bots

### QA

- [elastic](https://github.com/archie-yu/ChatBot/blob/master/chatbot/bot/elastic.py)

  - Based on FQA and tags match, using [Elasticsearch](https://github.com/elastic/elasticsearch) for searching tags.
  
  - Run Elasticsearch before using this bot.

- TODO

### Talk

- TODO

## Platforms

- [http](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/http.py)

  - Based on [Tornado](https://github.com/tornadoweb/tornado).
  
  - Support Wechat Mass Platform api.

- [wechat](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/wechat.py)

  - Based on [ItChat](https://github.com/littlecodersh/ItChat).
  
  - Got some login problems now.

- [wechatmp](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/wechatmp.py)

  - Based on [ItChatmp](https://github.com/littlecodersh/ItChatmp).

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
