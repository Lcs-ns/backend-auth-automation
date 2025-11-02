from typing import Optional
from sqlalchemy.future import select
from app.application.ports.user_repository import UserRepository
from app.domain.models import User
from app.infrastructure.repositories.db import AsyncSessionLocal
from app.infrastructure.models import UserORM

class PostgresUserRepository(UserRepository):
    async def save(self, user: User) -> None:
        async with AsyncSessionLocal() as session:
            async with session.begin():
                orm_user = UserORM(email=user.email, password_hash=user.password_hash)
                session.add(orm_user)

    async def find_by_email(self, email: str) -> Optional[User]:
        async with AsyncSessionLocal() as session:
            result = await session.execute(select(UserORM).where(UserORM.email == email))
            orm_user = result.scalars().first()
            if not orm_user:
                return None
            return User(email=orm_user.email, password_hash=orm_user.password_hash)
