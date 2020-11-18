class ResponseError:
    __error = ""

    # 设置一个错误
    def __setError(self, err):
        self.__error = err

    # 获取一个响应的错误
    def getError(self):
        err = self.__error
        self.__unsetError()
        return err

    # 设置响应错误
    def _setRequestError(self, err):
        self.__setError("[RequestError]:" + err)

    # 设置sdk错误
    def _setSdkError(self, err):
        self.__setError("[SDKError]:" + err)

    def __unsetError(self):
        self._error = ""
