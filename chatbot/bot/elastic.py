# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET

import jieba

from .abstract import Bot as AbstractBot
from ..settings import *
from ..util.elastic import Elastic


class Bot(AbstractBot):

    def __init__(self):
        assert QA_TYPE in ['question', 'tag']
        self.qa_type = QA_TYPE
        self.elastic = Elastic(INDEX)
        self.related = None
        logging.info('bot initialized.')
        jieba.enable_parallel(4)
        jieba.initialize()

    def init(self):
        self.create(delete_if_exist=True)
        self.load()
        logging.info("Elastic initialized.")

    def create(self, delete_if_exist=False):
        if self.elastic.exist():
            if delete_if_exist:
                self.elastic.delete()
            else:
                return
        self.elastic.create(mapping={
            'settings': {
                'similarity': {
                    'scripted_tfidf': {
                        'type': 'scripted',
                        'script': {
                            'source': 'double tf = Math.sqrt(doc.freq);'
                                      'double norm = 1/Math.sqrt(doc.length);'
                                      'return query.boost * tf * norm;'
                        }
                    }
                },
                'analysis': {
                    'filter': {
                        'single_gram_filter': {
                            'type': 'ngram',
                            'min_gram': 2
                        }
                    },
                    'analyzer': {
                        'ik_filter_single_gram': {
                            'type': 'custom',
                            'tokenizer': 'ik_max_word',
                            'filter': [
                                'single_gram_filter'
                            ]
                        }
                    }
                }
            },
            'mappings': {
                'properties': {
                    'question': {
                        'type': 'text',
                        'analyzer': 'ik_max_word',
                        'search_analyzer': 'ik_smart'
                    },
                    'tag': {
                        'type': 'text',
                        'analyzer': 'whitespace',
                        'similarity': 'scripted_tfidf'
                        # 'search_analyzer': 'ik_filter_single_gram'
                    },
                    'answer': {
                        'type': 'keyword'
                    }
                }
            }
        })

    def exist(self):
        return self.elastic.exist()

    def word(self, w):
        if not self.related:
            self.related = dict()
            f = open(PATH_RELATED_DIC, 'r')
            for line in f.readlines():
                words = line.strip().split(',')
                for word in words:
                    self.related[word] = words[0]
            f.close()
            logging.info('related word dictionary loaded.')
        return self.related.get(w)

    def load(self):
        tree = ET.parse(PATH_FQA)
        root = tree.getroot()
        def add(qas, default_answer=None):
            for qa in qas:
                if self.qa_type == 'question':
                    # question模式下，直接添加
                    keyword = qa.find('question').text
                else:
                    # tag模式下，需要先收集tag
                    keyword = []
                    for tag in qa.findall('tag'):
                        for child in tag:
                            keyword.append(child.text)
                # 无意义问题可以自定义统一回复
                if default_answer is None:
                    answer = ET.tostring(qa.find('answer'), encoding='utf-8').decode('utf-8')[8:-18].strip()
                self.elastic.add(action={
                    '_source': {
                        self.qa_type: keyword,
                        'answer': answer if default_answer is None else default_answer
                    }
                })
        add(root[0], TXT_MEANINGLESS_ANSWER)
        add(root[1])
        self.elastic.commit()

    def answer(self, uid, question):
        logging.info(f'Q: {question}')
        if self.qa_type == 'tag':
            seg_list = jieba.cut_for_search(question)
            tag_list = []
            for seg in seg_list:
                w = self.word(seg)
                if w:
                    tag_list.append(w)
                else:
                    tag_list.append(seg)
            body = {
                'query': {
                    'match': {
                        'tag': ' '.join(tag_list)
                    }
                },
                '_source': [
                    'tag',
                    'answer'
                ]
            }
        else:
            body = {
                'query': {
                    'match': {
                        'question': question
                    }
                },
                '_source': [
                    'question',
                    'answer'
                ]
            }
        hits = self.elastic.search(body=body)['hits']['hits']
        if len(hits) > 0:
            # tag模式下，检查是否匹配的标签数量是否超过阈值
            if self.qa_type == 'tag':
                matched = 0
                total = 0
                for tag in hits[0]['_source']['tag']:
                    total += 1
                    if tag in tag_list:
                        matched += 1
                if matched < limit(total):
                    return TXT_NO_ANSWER
            # question模式下，直接返回结果
            return hits[0]['_source']['answer']
        else:
            logging.error('no answer')
            return TXT_NO_ANSWER
