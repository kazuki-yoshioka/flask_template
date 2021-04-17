from ..utility.UtilityCheck import UtilityCheck
from ..model import ModelManager
from .login.LoginController import *
from .login.EnterLoginController import *


class ControllerManager:

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

        # ログイン中
        if 'userId' in session and session['userId'] is not None:
            return ""

        # パラメータにログインIDを持っている
        if request.json is not None and 'userId' in request.json:
            return ""

        # Index画面ではない
        if request.path != '/Login':
            if '.js' in request.path or '.css' in request.path:
                return ""

            if 'userId' not in session or session['userId'] is None:
                return "login"

        return ""

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

        return self.setResponeData(con)

    def setResponeData(self, con):
        response = {}
        response["model"] = con.model
        response["response"] = vars(con.model)
        response["nextUrl"] = con.model.nextUrl
        response["errMassageList"] = con.model.errMassageList
        return response

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
        splitPath = str(path).split("/")
        if type(splitPath) is not list:
            return str(path)

        pathStr = ""
        for _str in splitPath:
            pathStr = pathStr + _str

        pathStr = pathStr.replace("/", "")
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
            baseInstanceName = "Login"

        jsonIns = {}

        try:
            # モデルクラスを生成
            bModel = ModelManager.ModelManager()
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
        """[summary] リクエストを受けたパラメータをモデルにセット

        Args:
            session ([type]): [description] セッション
            request ([type]): [description] リクエストパラメータ
            jsonIns ([type]): [description] インスタンス

        Returns:
            [type]: [description]
        """
        modelIns = jsonIns["modelIns"]
        modelIns.setBaseModelFromParam(session, request)

        # モデルのフィールド値にパラメータをセット
        self.setModelProperty(modelIns, request.json)
        jsonIns["modelIns"] = modelIns

        return jsonIns

    def setModelProperty(self, _model, _requestJson=None):
        """[summary] モデルのプロパティ値にリクエストパラメータをセットする

        Args:
            _model ([type]): [description] モデル
            _requestJson ([type]): [description] リクエストパラメータ
        """
        if _requestJson is None:
            return

        for key in _requestJson:
            if UtilityCheck().isStr(key) is False:
                continue

            try:
                setattr(_model, str(key), _requestJson[str(key)])

            except Exception as e:
                print(str(key) + ": は存在しない項目")
                print(e)

        return
