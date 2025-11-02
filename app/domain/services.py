from passlib.hash import bcrypt

class PasswordService:
    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hash(password)
    
    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        return bcrypt.verify(password, hashed)