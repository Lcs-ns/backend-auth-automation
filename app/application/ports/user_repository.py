from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models import User

class UserRepository(ABC):
    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def find_by_email(self, email: str) -> Optional[User]:
        pass