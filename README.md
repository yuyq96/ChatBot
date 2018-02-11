# ChatBot

## [Bots](https://github.com/archie-yu/ChatBot/tree/master/chatbot/bot)

### QA

- [elastic](https://github.com/archie-yu/ChatBot/blob/master/chatbot/bot/elastic.py)

  - Based on FQA and tags match, using [Elasticsearch](https://github.com/elastic/elasticsearch) for searching tags.
  
  - Run Elasticsearch before using this bot.

- TODO

### Talk

- TODO

## [Service](https://github.com/archie-yu/ChatBot/tree/master/chatbot/util/service)

- [http](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/http.py)

  - Based on Tornado
  
  - Support Wechat public platform api

- [wechat](https://github.com/archie-yu/ChatBot/blob/master/chatbot/util/service/wechat.py)

  - Based on [ItChat](https://github.com/littlecodersh/ItChat), got some login problems now.

## Getting Started

### Settings

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

```cfg
[CUSTOM]
;elastic
;The FQA file path
PATH_FQA = xxx/FQA.xml
;The related word dictionary path
PATH_RELATED_DIC = xxx/related.dic
;The default return value if QABot can't find an proper answer
TXT_NO_ANSWER = Sorry, xxx.
;The default return value if question is meaningless
TXT_MEANINGLESS_ANSWER = Sorry, xxx.
;The minimum value of matched/total tags of a proper match
LIMIT_TAGS_MATCH = 0.8
```

### Demo

See [`demo.py`](https://github.com/archie-yu/ChatBot/blob/master/demo.py)

## License

[LGPL-3.0](https://github.com/archie-yu/ChatBot/blob/master/LICENSE)
