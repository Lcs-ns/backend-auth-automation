from app.domain.services import PasswordService
from app.application.ports.user_repository import UserRepository
from app.application.ports.auth_service import AuthService

class LoginUser:
    def __init__(self, user_repo: UserRepository, auth_service: AuthService):
        self.user_repo = user_repo
        self.auth_service = auth_service

    async def execute(self, email: str, password: str) -> str:
        user = await self.user_repo.find_by_email(email)
        if not user or not PasswordService.verify_password(password, user.password_hash):
            raise ValueError("Invalid credentials")

        return self.auth_service.create_token(user)