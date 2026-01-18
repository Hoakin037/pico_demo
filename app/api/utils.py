from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import HTTPException, Depends
from jwt import PyJWTError  
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from app.core import SECRET_KEY, ALGORITHM
from app.db import Users, get_db, get_user_rep