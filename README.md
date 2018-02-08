# QABot

## A Question &amp; Answering Bot

### Bots

- [elastic](https://github.com/archie-yu/QABot/blob/master/qabot/bot/elastic.py)

  Based on FQA and tags match, using [Elasticsearch](https://github.com/elastic/elasticsearch) for searching tags.
  
  Run Elasticsearch before using this bot.

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
```
MIT License

Copyright (c) 2018 Archie Yu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
