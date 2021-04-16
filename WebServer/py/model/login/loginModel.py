from ..baseModel import baseModel


class loginModel(baseModel):
    val = 100
    name = "ログイン"
    id = ""
    password = ""
    baseModel.displayTitle = "ログイン画面"
    baseModel.nextUrl = "login"
