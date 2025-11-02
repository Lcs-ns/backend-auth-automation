from abc import ABC, abstractmethod
from app.domain.models import User

class AuthService(ABC):
    @abstractmethod
    def create_token(self, user: User) -> str:
        pass