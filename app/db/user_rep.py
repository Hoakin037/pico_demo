from db.models import Users
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException

class UserRepository():

    async def user_add(self, user: Users, db: AsyncSession):

        db.add(user)
        await db.commit()
        await db.refresh(user) 

    async def user_update_token(self, user: Users, token: str, db: AsyncSession):

        user.refresh_token = token
        user.is_active = True
        db.commit()
        db.refresh(user)

        
    async def user_get(self, email: str, db: AsyncSession) -> Users:
        try:
            result = await db.execute(select(Users).where(Users.email==email))
            existing_user = result.scalars().first()
            if existing_user:
                return existing_user
            return None
        except Exception:
            raise HTTPException(status_code=500, detail="Ошибка обращения к БД!")
        
    async def user_update_pass(self, user: Users, new_password: str, db: AsyncSession):
        
        user.password = new_password
        await db.commit()
        await db.refresh(user)

        
    async def user_delete(self, user: Users, db: AsyncSession):
        await db.delete(user)
        await db.commit()
        
        
async def get_user_rep():
    return UserRepository()