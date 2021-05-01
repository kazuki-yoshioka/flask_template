class BaseController:
    model = {}

    def __init__(self, _model):
        self.model = _model

    def setModel(self, _model):
        """[summary] モデルをセットする

        Args:
            _model ([type]): [description]
        """
        self.model = _model

    def getModel(self):
        """[summary] モデルを返却

        Returns:
            [type]: [description]
        """
        return self.model

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

    def addErrorMessage(self, message):
        """[summary] 画面に表示するメッセージを設定する

        Args:
            message ([type]): [description]
            メッセージ
        """
        self.model.errMassageList.append(str(message))

    def addNormalMessage(self, message):
        """[summary] 画面に表示するメッセージを設定する

        Args:
            message ([type]): [description]
            メッセージ
        """
        self.model.errMassageList.append(str(message))
