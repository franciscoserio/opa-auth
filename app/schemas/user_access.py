from pydantic import BaseModel


class UserInfo(BaseModel):
    username: str
    role: str


class UserAccessResponse(BaseModel):
    hasAccess: bool
