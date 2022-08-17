from abc import ABC, abstractmethod


class IPlugin(ABC):
    @abstractmethod
    def initialize(self) -> None:
        pass

    @abstractmethod
    def deinitialize(self) -> None:
        pass
