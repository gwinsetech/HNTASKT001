from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserInfo(BaseModel):
    """User information model"""
    email: str
    name: str
    stack: str


class ProfileResponse(BaseModel):
    """Profile endpoint response model"""
    status: str
    user: UserInfo
    timestamp: str
    fact: str


class CatFactResponse(BaseModel):
    """Cat Facts API response model"""
    fact: str
    length: int

