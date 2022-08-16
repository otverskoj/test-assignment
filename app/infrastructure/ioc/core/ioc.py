from typing import Type, TypeVar, Dict
from abc import abstractmethod, ABC


__all__ = ('IIoc',)


T = TypeVar('T')


class IIoc(ABC):
    __slots__ = ()

    @abstractmethod
    def set_instance(self, instance_type: Type[T], instance: T) -> None:
        pass

    @abstractmethod
    def get_instance(self, instance_type: Type[T]) -> T:
        pass

    @abstractmethod
    def delete_instance(self, instance_type: Type[T]) -> None:
        pass

    @abstractmethod
    def delete_all_instances(self):
        pass
