from ..model import baseModel
from ..model import modelManager
from .login.loginController import *
import inspect


class controllerManager:

    """[summary]
        処理名称
            init
            move
            search
            fetch
            regist
            update
            export
    Returns:
        [type]: [description]
    """
    processingList = []

    def __init__(self):
        """[summary] 初期処理
        """
        self.processingList.append("init/")
        self.processingList.append("move/")
        self.processingList.append("search/")
        self.processingList.append("fetch/")
        self.processingList.append("regist/")
        self.processingList.append("update/")
        self.processingList.append("export/")

    def beforeRequest(self, session={}, request={}):
        """[summary]
            リクエストされたときの初期処理
            初回接続やセッション切れの場合、ログイン画面へ遷移する
        Args:
            session ([type]): [description] セッション
            request ([type]): [description] リクエストパラメータ

        Returns:
            [type]: [description]
        """
        # セッション切れ
        if 'siteFlg' not in session:
            session['siteFlg'] = True
            return "login"

        # Index画面ではない
        if request.path != '/':
            if '.js' in request.path or '.css' in request.path:
                return ""

            if 'userId' not in session or session['userId'] is None:
                return "login"

    def execute(self, session, request):
        """[summary] 処理を実行する

        Args:
            session ([type]): [description]　セッション情報
            request ([type]): [description]　リクエストパラメータ

        Returns:
            [type]: [description]
        """

        # 初期処理（コントローラ、モデルクラスを生成）
        instanceJson = self.initExecute(session, request)
        if instanceJson is None:
            return

        con = instanceJson['controllerIns']

        if False is con.validate():
            # todo エラー処理
            return

        try:
            con.execute()
        except NameError as e:
            print(e)
        except Exception as e:  # これは最後に書く
            print('Unknown exception!')
            print(e)

        con.after()

        session["response"] = con.getModel().response
        if con.getModel().nextUrl is None or con.getModel().nextUrl == "":
            session["nextUrl"] = con.getModel().nextUrl

        return

    def initExecute(self, session, request):
        """[summary] 初期処理

        Args:
            session ([type]): [description]
            request ([type]): [description]

        Returns:
            [type]: [description]
        """
        baseInstanceName = self.getBaseInstanceName(str(request.path))

        if(baseInstanceName is None or "" == baseInstanceName):
            return None

        # コントローラ、モデルクラスを生成
        jsonIns = self.createClass(baseInstanceName)

        if jsonIns is None:
            return None

        # todo コントローラ、モデルクラスのチェック処理

        jsonIns = self.setModelFromParam(session, request, jsonIns)
        return jsonIns

    def getBaseInstanceName(self, path):
        """[summary]
                コントローラ、モデルのベースとなるクラス名の文字列を返却する
        Args:
            path ([type]): [description]　urlパス

        Returns:
            [type]: [description]
        """
        pathStr = str(path)
        for processing in self.processingList:
            pathStr = pathStr.replace(str(processing), "")

        return pathStr

    def createClass(self, baseInstanceName):
        """[summary]
            コントローラ、モデルクラスを返却する
        Args:
            baseInstanceName ([type]): [description]
                基準クラス文字列

        Returns:
            [type]: [description]
        """
        # urlが見つからない
        if baseInstanceName is None:
            return None

        if baseInstanceName == "/":
            baseInstanceName = "login"

        jsonIns = {}

        try:
            # モデルクラスを生成
            bModel = modelManager.modelManager()
            modelIns = bModel.getExecuteModel(baseInstanceName)

            # コントローラクラスを生成
            cls = globals()[baseInstanceName + "Controller"]
            controllerIns = cls(modelIns)

            jsonIns = {"modelIns": modelIns, "controllerIns": controllerIns}

        except NameError as e:
            print(e)
        except Exception as e:  # これは最後に書く
            print('Unknown exception!')
            print(e)

        return jsonIns

    def setModelFromParam(self, session, request, jsonIns):
        modelIns = jsonIns["modelIns"]
        modelIns.setBaseModelFromParam(session, request)
        jsonIns["modelIns"] = modelIns

        return jsonIns
