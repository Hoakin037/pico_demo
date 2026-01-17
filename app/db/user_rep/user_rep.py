from app.models import Users
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException
from .data_models import UserCreate, UserDel, UserGet, UserUpdate, UserUpdatePass, UserUpdateRefToken

class UserRepository():

    async def user_add(self, data: UserCreate, db: AsyncSession):
        user = Users(email=data.email, name=data.name, surname=data.surname, password=data.password)

        existing_user = await self.user_get(user.email, db)
        if existing_user != None:
           raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")

        db.add(user)
        await db.commit()
        await db.refresh(user) 


    async def user_get(self, data: UserGet, db: AsyncSession) -> Users:
        try:
            result = await db.execute(select(Users).where(Users.email==data.email))
            existing_user = result.scalars().first()
            if existing_user:
                return existing_user
            return None
        except Exception:
            raise HTTPException(status_code=500, detail="Ошибка обращения к БД!")
        
    async def user_update_pass(self, data: UserUpdatePass, db: AsyncSession):
        exicting_user = await self.user_get(data.email, db)
        if exicting_user != None and exicting_user.password == data.current_pass:
            exicting_user.password = data.new_pass
            await db.commit()
        else:
            raise HTTPException(status_code=404, detail="Пользователь не найден или неверный пароль!")
        
    async def user_delete(self, data: UserDel, db: AsyncSession):
        existing_user = await self.user_get(data.email, db)
        if existing_user != None and existing_user.password == data.current_pass:
            await db.delete(existing_user)
            await db.commit()
        else:
            raise HTTPException(status_code=404, detail="Пользователь не найден или неверный пароль!")
        
async def get_user_rep():
    return UserRepository()