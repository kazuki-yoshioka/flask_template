class UtilityCheck(object):
    """[summary] ユーティリティのチェック処理

    Args:
        object ([type]): [description]
    """

    def isNone(self, _value):
        """[summary]  変数がNoneかチェック

        Args:
            value ([type]): [description]

        Returns:
            [type]: [description]
        """
        if _value is None:
            return False

        return True

    def isStr(self, _str):
        """[summary] 変数が文字列かチェック

        Args:
            _str ([type]): [description]

        Returns: True：文字列
            [type]: [description]
        """
        if self.isNone(_str) is False:
            return False

        if type(_str) is not str:
            return False

        return True

    def isInt(self, _value):
        """[summary] 変数が整数かチェックする

        Args:
            _value ([type]): [description]

        Returns:
            [type]: [description]
        """
        if self.isNone(_value) is False:
            return False

        if type(_value) is not int:
            return False

        return True
