from abc import ABC, abstractmethod


class OpenAIBasicRepository(ABC):

    @abstractmethod
    def generateText(self, userSendMessage):
        pass

    @abstractmethod
    def audioAnalysis(self, file):
        pass