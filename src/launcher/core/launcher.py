from abc import ABC, abstractmethod


class ILauncher(ABC):
    __slots__ = ()

    @abstractmethod
    def handle_startup(self) -> None:
        pass

    @abstractmethod
    def handle_shutdown(self) -> None:
        pass
