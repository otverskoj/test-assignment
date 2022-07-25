from app.storage.base_repository import UserRepository
from app.storage.user_in_memory_repository import UserInMemoryRepository
from app.storage.user_db_repository import UserDBRepository
from app.settings import REPOSITORY_TYPE


_repositories = {
    'in_memory': UserInMemoryRepository,
    'db': UserDBRepository
}


repository: UserRepository = _repositories[REPOSITORY_TYPE]()
