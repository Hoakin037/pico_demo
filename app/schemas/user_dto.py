from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    email: EmailStr = Field(max_length=255)

class UserCreate(UserBase):
    name: str = Field(max_length=255)
    surname: str = Field(max_length=255)
    password: str = Field(max_length=128)

class UserUpdate(BaseModel):
    current_email: str = Field(max_length=255)
    new_email: str = Field(max_length=255, default="")
    name: str = Field(max_length=255, default="")
    surname: str = Field(max_length=255, default="")

class UserDel(UserBase):
    password: str = Field(max_length=128)

class UserUpdatePass(UserBase):
    current_pass: str = Field(max_length=128)
    new_pass: str = Field(max_length=128)

class UserUpdateRefToken(UserBase):
    new_token: str = Field(max_length=255)
    