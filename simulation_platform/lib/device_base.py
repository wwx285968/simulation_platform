from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def report_state(self):
        pass
