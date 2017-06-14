
from os import listdir
from os.path import join, dirname
import math

from textblob import TextBlob as tb
from . import DataHandler

class Interpreter:
    def __init__(self, base, **kwargs):
        self.base = base
        if "data file" in kwargs:
            self.data_file = kwargs["data file"]
        else:
            self.data_file = join(dirname(__file__), "../data/default_data.dat")
        self.data_handler = DataHandler(base, self.data_file)

    def interpret(self, message):
        """ This function is the main calling point when a message is to be interpreted. As of now
        the only method of message interpretation/ document classification is using TF/IDF. But if
        other methods are added later this will be the forking point.
        """
        self.base.log("Interpreting using TF/IDF")
        return self.best_match_tfidf(message)

    def best_match_tfidf(self, message):
        """ Message classification using TF/IDF
        """
        doc_list = self.data_handler.get_doc_list()
        best_score = 0
        best_topic = ""
        for topic in self.data_handler.topics.keys():
            doc = self.data_handler.topics[topic]["keywords"]
            score = sum(self.tfidf(word, doc, doc_list) for word in message.split(" "))
            if score > best_score:
                best_score = score
                best_topic = topic
        if best_score == 0:
            return self.data_handler.get_default_action()
        else:
            return self.data_handler.topics[best_topic]["action"]

    def tf(self, word, blob):
        """ Calculate the term frequency.
        """
        return blob.words.count(word) / len(blob.words)

    def n_containing(self, word, doc_list):
        """ Calculate the number of times 'word' occurs in the corpus.
        """
        return sum(1 for doc in doc_list if word in doc.words)

    def idf(self, word, doc_list):
        """ Calculate the inverse document frequency.
        """
        return math.log(len(doc_list) / (1 + self.n_containing(word, doc_list)))

    def tfidf(self, word, doc, doc_list):
        """ Calculate the term frequency / inverse document frequency for 'word'.
        """
        return self.tf(word, doc) * self.idf(word, doc_list)
