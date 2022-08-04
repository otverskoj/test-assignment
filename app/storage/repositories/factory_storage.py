from app.storage.repositories.repository_factory import IUserRepositoryFactory
from app.storage.repositories.in_memory.factory import UserInMemoryRepositoryFactory
from app.storage.repositories.postgres.factory import UserPostgresRepositoryFactory
from app.errors.factory_not_registered import FactoryNotRegistered


class UserRepositoryFactoryStorage:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(UserRepositoryFactoryStorage, cls).__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.factories = {
            'in_memory': UserInMemoryRepositoryFactory(),
            'postgres': UserPostgresRepositoryFactory()
        }
    
    def get_factory(self, repo_type: str) -> IUserRepositoryFactory:
        if repo_type in self.factories:
            return self.factories[repo_type]
        raise FactoryNotRegistered(f'Factory for "{repo_type}" repository is not registered')

    def register_factory(
        self, 
        repo_type: str, 
        fac: IUserRepositoryFactory
    ) -> None:
        self.factories[repo_type] = fac

    def unregister_factory(self, repo_type: str) -> None:
        if repo_type in self.factories:
            del self.factories[repo_type]
        else:
            raise FactoryNotRegistered(
                f'Factory "{repo_type}" is not registered'
            )
