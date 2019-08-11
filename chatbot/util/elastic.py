# -*- coding: utf-8 -*-
import logging

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class Elastic:

    es = Elasticsearch()
    actions = []

    def __init__(self, index):
        self.index = index
        self.count = 0

    def create(self, mapping):
        if not self.exist():
            if self.es.indices.create(index=self.index, body=mapping):
                logging.info("Create index succeed.")
                return True
            else:
                logging.error("Create index failed.")
                return False
        else:
            logging.info("Target index already exist.")
            return False

    def delete(self):
        if self.exist():
            if self.es.indices.delete(self.index):
                logging.info("Delete index succeed.")
                return True
            else:
                logging.info("Delete index failed.")
                return False
        else:
            logging.info("Target index not exist.")
            return False

    def exist(self):
        return self.es.indices.exists(self.index)

    def add(self, action):
        self.actions.append(action)
        if len(self.actions) >= 100:
            self.commit()

    def search(self, body, doc_type=None):
        if doc_type is not None:
            return self.es.search(index=self.index, doc_type=doc_type, body=body)
        else:
            return self.es.search(index=self.index, body=body)

    def commit(self):
        success, error = bulk(self.es, self.actions, index=self.index, raise_on_error=True)
        self.actions = []
        self.count += success
        logging.info("Performed %d actions, total %s." % (success, self.count))
