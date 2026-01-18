from db.models import Users
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import HTTPException, Depends
from app.schemas import UserCreate, UserDel, UserBase, UserUpdate, UserUpdatePass, UserUpdateRefToken
from app.db import get_user_rep, UserRepository


class UserService():
    async def user_get(self, data: UserBase, db: AsyncSession, rep: UserRepository = Depends(get_user_rep)):
        try:
            await rep.user_get(data.email, db)
        except Exception as e:
            raise e
    
    async def user_add(self, data: UserCreate, db: AsyncSession, rep: UserRepository = Depends(get_user_rep)):

        user = Users(email=data.email, name=data.name, surname=data.surname, password=data.password)

        existing_user = await self.user_get(user.email, db)
        if existing_user != None:
           raise HTTPException(status_code=400, detail="Пользователь с таким email уже существует!")
        
        await rep.user_add(user, db)

    async def user_update_token(self, data: UserUpdateRefToken, db: AsyncSession, rep: UserRepository = Depends(get_user_rep)):

        existing_user = await self.user_get(data.email, db)
        if existing_user != None:
            await rep.user_update_token(existing_user, data.new_token, db)
        else:
            raise HTTPException(status_code=404, detail="Пользователь не найден!")
        
    async def user_update_pass(self, data: UserUpdatePass, db: AsyncSession, rep: UserRepository = Depends(get_user_rep)):
        
        existing_user = await self.user_get(data.email, db)
        if existing_user != None:
            if existing_user.password != data.current_pass:
                raise HTTPException(status_code=401, detail="Неверный пароль!")
            await rep.user_update_pass(existing_user, data.new_pass, db)
        else:
            raise HTTPException(status_code=404, detail="Пользователь не найден!")    
        
    async def user_delete(self, data: UserDel, db: AsyncSession, rep: UserRepository = Depends(get_user_rep)):

        existing_user = await self.user_get(data.email, db)
        if existing_user != None:
            if existing_user.password != data.current_pass:
                raise HTTPException(status_code=401, detail="Неверный пароль!")
            await rep.user_delete(existing_user, db)
        else:
            raise HTTPException(status_code=404, detail="Пользователь не найден!")  
        
def get_user_service():
    return UserService()