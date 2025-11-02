from fastapi import APIRouter, HTTPException
from app.api.schemas.auth import RegisterRequest, LoginRequest
from app.application.use_cases.register_user import RegisterUser
from app.application.use_cases.login_user import LoginUser
from app.infrastructure.repositories.user_repository import PostgresUserRepository
from app.infrastructure.security.jwt_service import JWTService

router = APIRouter()
user_repo = PostgresUserRepository()
jwt_service = JWTService()

register_user_uc = RegisterUser(user_repo)
login_user_uc = LoginUser(user_repo, jwt_service)

@router.post("/register")
async def register(data: RegisterRequest):
    try:
        user = await register_user_uc.execute(data.email, data.password)
        return {"email": user.email}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/login")
async def login(data: LoginRequest):
    try:
        token = await login_user_uc.execute(data.email, data.password)
        return {"token": token}
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))