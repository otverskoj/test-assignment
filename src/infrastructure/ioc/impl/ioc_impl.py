from typing import Type, TypeVar, Dict

from src.infrastructure.ioc.core.ioc import IIoc


__all__ = ('ioc',)


T = TypeVar('T')


class IocImpl(IIoc):
    __slots__ = ('__instances',)

    def __init__(self) -> None:
        self.__instances: Dict[Type[T], T] = {}

    def set_instance(self, instance_type: Type[T], instance: T) -> None:
        if not isinstance(instance, instance_type):
            raise TypeError(
                f"The specified instance {instance} is not a subtype of the {instance_type}."
            )
        self.__instances[instance_type] = instance

    def get_instance(self, instance_type: Type[T]) -> T:
        if instance_type in self.__instances:
            return self.__instances[instance_type]
        raise KeyError(f'Instance of type {instance_type} not registered')

    def delete_instance(self, instance_type: Type[T]) -> None:
        if instance_type not in self.__instances:
            raise KeyError(f'Instance of type {instance_type} not registered')
        self.__instances.pop(instance_type, None)

    def delete_all_instances(self):
        self.__instances.clear()


ioc = IocImpl()
