# QABot

## Question &amp; Answering Bots

### Bots

- [elastic](https://github.com/archie-yu/QABot/blob/master/qabot/bot/elastic.py)

  - Based on FQA and tags match, using [Elasticsearch](https://github.com/elastic/elasticsearch) for searching tags.
  
  - Run Elasticsearch before using this bot.

- TODO

## Getting Started

### Demo
See [`demo.py`](https://github.com/archie-yu/QABot/blob/master/demo.py)

### Settings
Configure [`QABot.cfg`](https://github.com/archie-yu/QABot/blob/master/QABot.cfg)
```cfg
[CUSTOM]
;The FQA file path
PATH_FQA = xxx/FQA.xml
;The related word dictionary path
PATH_RELATED_DIC = xxx/related.dic
;The default return value if QABot can't find an proper answer
TXT_NO_ANSWER = Sorry, xxx.
```

## License
[LGPL-3.0](https://github.com/archie-yu/QABot/blob/master/LICENSE)
