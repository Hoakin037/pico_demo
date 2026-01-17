from . import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta, timezone
from jwt import encode
from typing import Literal
from pydantic import BaseModel, Field, EmailStr

class Payload(BaseModel):
    email: EmailStr = Field(max_length=255)
    name: str = Field(max_length=255)
    surname: str = Field(max_length=255)

def create_token(payload: Payload, token_type: Literal["refresh", "access"],expires_delta: timedelta | None = None):
    payload = payload.model_dump()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=30))
    payload.update({'exp': expire, 'type': token_type})

    return encode(payload, SECRET_KEY, algorithm=ALGORITHM)