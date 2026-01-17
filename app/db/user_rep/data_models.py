from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    email: str = Field(max_length=255)
    name: str = Field(max_length=255)
    surname: str = Field(max_length=255)
    password: str = Field(max_length=255)

class UserGet(BaseModel):
    email: str = Field(max_length=255)

class UserUpdate(BaseModel):
    current_email: str = Field(max_length=255)
    new_email: str = Field(max_length=255, default="")
    name: str = Field(max_length=255, default="")
    surname: str = Field(max_length=255, default="")

class UserDel(BaseModel):
    email: str = Field(max_length=255)
    password: str = Field(max_length=255)

class UserUpdatePass(BaseModel):
    email: str = Field(max_length=255)
    current_pass: str = Field(max_length=255)
    new_pass: str = Field(max_length=255)

class UserUpdateRefToken(BaseModel):
    email: str = Field(max_length=255)
    new_token: str = Field(max_length=255)
