# -*- coding: utf-8 -*-
import logging

import jieba
from ..settings import *
from ..util.elastic import Elastic
import xml.etree.ElementTree as ET


class Bot:
    def __init__(self):
        self.elastic = Elastic("qabot")
        self.doc_type = "fqa"
        self.related = None
        logging.info("Bot initialized.")
        jieba.enable_parallel(4)
        jieba.initialize()

    def create(self, delete_if_exist=False):
        if self.elastic.exist():
            if delete_if_exist:
                self.elastic.delete()
            else:
                return
        self.elastic.create(mapping={
            "settings": {
                "similarity": {
                    "scripted_tfidf": {
                        "type": "scripted",
                        "script": {
                            "source": "double tf = Math.sqrt(doc.freq);"
                                      "double norm = 1/Math.sqrt(doc.length);"
                                      "return query.boost * tf * norm;"
                        }
                    }
                },
                "analysis": {
                    "filter": {
                        "single_gram_filter": {
                            "type": "ngram",
                            "min_gram": 2
                        }
                    },
                    "analyzer": {
                        "ik_filter_single_gram": {
                            "type": "custom",
                            "tokenizer": "ik_max_word",
                            "filter": [
                                "single_gram_filter"
                            ]
                        }
                    }
                }
            },
            "mappings": {
                self.doc_type: {
                    "properties": {
                        "question": {
                            "type": "keyword"
                        },
                        "tag": {
                            "type": "text",
                            "analyzer": "whitespace",
                            "similarity": "scripted_tfidf"
                            # "search_analyzer": "ik_filter_single_gram"
                        },
                        "answer": {
                            "type": "keyword"
                        }
                    }
                }
            }
        })

    def exist(self):
        return self.elastic.exist()

    def word(self, w):
        if not self.related:
            self.related = dict()
            f = open(PATH_RELATED_DIC, "r")
            for line in f.readlines():
                words = line.strip().split(",")
                for word in words:
                    self.related[word] = words[0]
            f.close()
            logging.info("Related word dictionary loaded.")
        return self.related.get(w)

    def load(self):
        tree = ET.parse(PATH_FQA)
        root = tree.getroot()
        meaningless = root[0]
        for qa in meaningless:
            for tag in qa.iter("tag"):
                for child in tag:
                    self.elastic.add(action={
                        "_type": self.doc_type,
                        "_source": {
                            "tag": child.text,
                            "answer": TXT_NO_ANSWER
                        }
                    })
        meaningful = root[1]
        for qa in meaningful:
            question = qa.find("question").text
            tags = []
            for tag in qa.findall("tag"):
                for child in tag:
                    tags.append(child.text)
            answer = ET.tostring(qa.find("answer"), encoding="utf-8").decode("utf-8")[8:-12].strip()
            self.elastic.add(action={
                "_type": self.doc_type,
                "_source": {
                    "question": question,
                    "tag": tags,
                    "answer": answer
                }
            })
        self.elastic.commit()

    def init_elastic(self):
        self.create(delete_if_exist=True)
        self.load()
        logging.info("Elastic initialized.")

    def answer(self, question):
        logging.info("Question '%s'" % question)
        seg_list = jieba.cut_for_search(question)
        tag_list = []
        for seg in seg_list:
            w = self.word(seg)
            if w:
                tag_list.append(w)
            else:
                tag_list.append(seg)
        body = {
            "query": {
                "match": {
                    "tag": " ".join(tag_list)
                }
            },
            "_source": [
                "tag",
                "answer"
            ]
        }
        hits = self.elastic.search(doc_type=self.doc_type, body=body)["hits"]["hits"]
        if len(hits) > 0:
            matched = 0
            total = 0
            for tag in hits[0]["_source"]["tag"]:
                total += 1
                if tag in tag_list:
                    matched += 1
            if matched >= limit(total):
                return hits[0]["_source"]["answer"]
            return TXT_NO_ANSWER

        else:
            logging.error("Question '%s' has no answer." % question)
            return TXT_NO_ANSWER
