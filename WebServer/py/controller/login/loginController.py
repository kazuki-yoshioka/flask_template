from ...model.login.loginModel import loginModel
from ..baseController import baseController


class loginController(baseController):
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
        return True

    def after(self):
        """[summary] 後処理

        Returns:
            [type]: [description]
        """
        print("after")
        return True
