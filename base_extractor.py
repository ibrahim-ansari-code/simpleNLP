from abc import ABC, abstractmethod


class BaseExtractor(ABC):
    @abstractmethod
    def extractSpan(self, question, sentence):
        pass
