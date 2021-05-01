

class BaseModel(object):
    nextUrl = ""
    displayTitle = ""
    sessionData = {}
    request = {}
    response = {}
    errMassageList = []
    normalMassageList = []
    requestData = {}
    loginModel = {}

    def __init__(self):
        self.sessionData = {}
        self.request = {}
        self.response = {}
        self.errMassageList = []
        self.normalMassageList = []

    def setBaseModelFromParam(self, session, request):
        if 'response' in session:
            self.sessionData = session["response"]

        if request is not None:
            self.request = request

            if request.json is not None:
                self.requestData = request.json

    def getExecuteModel(self, baseInstanceName):
        """[summary] 実行用のモデルを返却

        Args:
            baseInstanceName ([type]): [description]　インスタンス名

        Returns:
            [type]: [description]
        """
        cls = globals()[baseInstanceName + "Model"]
        modelIns = cls()
        return modelIns

    def setLoginModel(self, _model):
        """[summary] ログイン情報を保持する

        Args:
            _model ([type]): [description]
        """
        self.loginModel = _model
