from datetime import datetime, timedelta
from jose import jwt
from app.config.settings import settings
from app.domain.models import User
from app.application.ports.auth_service import AuthService

class JWTService(AuthService):
    def __init__(self):
        self.secret = settings.JWT_SECRET
        self.algorithm = "HS256"
        self.expires_hours = settings.JWT_EXPIRES_HOURS

    def create_token(self, user: User) -> str:
        payload = {
            "sub": user.email,
            "exp": datetime.utcnow() + timedelta(hours=self.expires_hours)
        }
        return jwt.encode(payload, self.secret, algorithm=self.algorithm)