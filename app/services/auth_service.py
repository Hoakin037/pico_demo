from sqlalchemy.ext.asyncio import AsyncSession
from app.core import password_hash
from app.db import get_user_rep

class AuthService:
    def __init__(self):
        self.service = get_user_rep()

    async def register_new_user(self):
        pass

    # добавить в Users is_active
    