import importlib.machinery as imm
import importlib
from .login.loginModel import *
import inspect


class modelManager:

    def __init__(self):
        print('exeute')

    def getExecuteModel(self, baseInstanceName):
        """[summary] 実行用のモデルを返却

        Args:
            baseInstanceName ([type]): [description]　インスタンス名

        Returns:
            [type]: [description]
        """
        cls = globals()[baseInstanceName + 'Model']
        modelIns = cls()
        return modelIns
