from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.sql import func
from app.db import Base
from sqlalchemy import String, Integer, ForeignKey, Column, DateTime


class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    surname: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))

    users_chats = relationship("UsersChats", back_populates='users')

class Chats(Base):
    __tablename__ = "chats"

    id: Mapped[int] = mapped_column(primary_key=True)
    
    users_chats = relationship("UsersChats", back_populates='chats')


class UsersChats(Base):
    __tablename__ = 'users_chats'
    user_id = Column(Integer, ForeignKey('users.id'), primary_key = True)
    chat_id = Column(Integer, ForeignKey('chats.id'), primary_key=True)

    user = relationship('Users', back_populates="users_chats")
    chats = relationship('Chats', back_populates='users_chats')

class Messages(Base):
    __tablename__ = "messages"
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String(4000)) 
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    users_chats_messages = relationship('UsersChatsMessages', back_populates="messages")

class UsersChatsMessages(Base):
    Column(Integer, ForeignKey('users.id'), primary_key = True)
    chat_id = Column(Integer, ForeignKey('chats.id'), primary_key=True)
    message_id = Column(Integer, ForeignKey('Messages.id'), primary_key=True)

    user = relationship('Users', back_populates="users_chats_messages")
    chats = relationship('Chats', back_populates='users_chats_messages')
    messages = relationship('Messages', back_populates='users_chats_messages')

