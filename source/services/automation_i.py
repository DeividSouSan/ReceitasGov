from abc import ABC, abstractmethod


class AutomationI(ABC):
    @staticmethod
    @abstractmethod
    def start():
        pass
