from ...model.login.EnterLoginModel import EnterLoginModel
from ..BaseController import BaseController


class EnterLoginController(BaseController):
    val = 100

    def validate(self):
        """[summary] バリデーションチェック
        """
        print(self.model)
        if self.model.userId != "aaa":
            self.addErrorMessage("IDが見つかりません。")
            return False

        if self.model.password != "123":
            self.addErrorMessage("パスワードが間違っています。")
            return False

        return True

    def execute(self):
        """[summary] 処理を実行

        Returns:
            [type]: [description]
        """
        print("execute")
        _model = {}
        _model["userId"] = self.model.userId
        _model["userName"] = "テスト名前"

        # ログイン情報を保持する
        self.model.setLoginModel(_model)

        # 次画面をセットする
        self.model.nextUrl = "Menu/Menu"

        return

    def after(self):
        """[summary] 後処理

        Returns:
            [type]: [description]
        """
        print("after")
        return True
