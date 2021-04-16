

class baseModel(object):
    nextUrl = ""
    displayTitle = ""
    sessionData = {}
    request = {}
    response = {}
    errMassageList = []

    def __init__(self):
        self.sessionData = {}
        self.request = {}
        self.response = {}
        self.errMassageList = []

    def setBaseModelFromParam(self, session, request):
        if 'response' in session:
            self.sessionData = session["response"]

        if request is not None:
            self.request = request

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
