# QABot

## Question &amp; Answering Bots

### Bots

- [elastic](https://github.com/archie-yu/QABot/blob/master/qabot/bot/elastic.py)

  - Based on FQA and tags match, using [Elasticsearch](https://github.com/elastic/elasticsearch) for searching tags.
  
  - Run Elasticsearch before using this bot.

- TODO

## Getting Started

### Settings

- Clone project

```
git clone https://github.com/archie-yu/QABot.git
```

- Copy [`QABot.cfg.template`](https://github.com/archie-yu/QABot/blob/master/QABot.cfg.template) to `QABot.cfg`

```
cd QABot
cp QABot.cfg.template QABot.cfg
```

- Configure `QABot.cfg`

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

See [`demo.py`](https://github.com/archie-yu/QABot/blob/master/demo.py)

## License

[LGPL-3.0](https://github.com/archie-yu/QABot/blob/master/LICENSE)
