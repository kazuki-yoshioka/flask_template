from ...model.login.LoginModel import LoginModel
from ..BaseController import BaseController


class LoginController(BaseController):
    val = 100

    def validate(self):
        """[summary] バリデーションチェック
        """
        print(self.model)
        return True

    def execute(self):
        """[summary] 処理を実行

        Returns:
            [type]: [description]
        """
        print("execute")
        self.model.nextUrl = "Login"
        return True

    def after(self):
        """[summary] 後処理

        Returns:
            [type]: [description]
        """
        print("after")
        return True
