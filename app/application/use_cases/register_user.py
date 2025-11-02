from app.domain.models import User
from app.domain.services import PasswordService
from app.application.ports.user_repository import UserRepository

class RegisterUser:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def execute(self, email: str, password: str):
        if await self.user_repo.find_by_email(email):
            raise ValueError("User already exists")

        hashed = PasswordService.hash_password(password)
        user = User(email=email, password_hash=hashed)
        await self.user_repo.save(user)
        return user
