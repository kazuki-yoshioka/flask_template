from ..BaseModel import BaseModel


class LoginModel(BaseModel):
    val = 100
    name = "ログイン"
    userId = ""
    password = ""
    BaseModel.displayTitle = "ログイン画面"
    BaseModel.nextUrl = "login"
