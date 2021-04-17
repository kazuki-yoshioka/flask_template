from .LoginModel import LoginModel


class EnterLoginModel(LoginModel):
    val = 100
    name = "ログイン"
    id = ""
    password = ""
    LoginModel.displayTitle = "ログイン画面"
    LoginModel.nextUrl = "login"
