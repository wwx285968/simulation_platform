from abc import ABC, abstractmethod


class Commucation(ABC):
    @abstractmethod
    def receive_cmd(self):
        pass

    @abstractmethod
    def report_state(self):
        pass
