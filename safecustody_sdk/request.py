import requests
import json
import urllib3

# 请求路由类
from safecustody_sdk.error import ResponseError

from safecustody_sdk.user import User


class Request(ResponseError):
    _user: User

    _host = ""

    def __init__(self, user: User):
        pass

    # 发起请求
    def _request(self, method, param):
        str = ""
        param = self.__requestParam(param, user=self._user)

        if param is not None and len(param) > 0 and param is not "":
            str = json.dumps(param)

        url = self._getUrl(method)
        if url is None or url is "":
            self._setSdkError("url is None")
            return None, self.getError()
        r = self.__post(url, str)
        if r is None:
            self._setSdkError("请求参数返回为空")
            return None, self.getError()

        r = self.__parseResp(r.text)
        return r, self.getError()

    # 提交post
    def __post(self, url, s):
        try:
            urllib3.disable_warnings()
            headers = {"Content-Type": "application/json"}
            r = requests.post(url, data=s, headers=headers, verify=False)
        except Exception as error:
            self._setSdkError(error)
            return None
        return r

    # 请求参数
    def __requestParam(self, param, user: User):
        arr = {
            "appid": user.getAppid(),
            "cryptype": 0,
        }

        data = {
            "auth": {
                "token": user.getAuth(),
                "timestamp": user.getTime()
            }
        }
        if param is not None and param is not "":
            data = {**data, **param}

        arr["data"] = data

        self._user.unsetTime()

        return arr

    # 解析响应参数
    def __parseResp(self, param):
        if param is None or param is "":
            self._setSdkError("解析失败,返回值是空")
            return None

        resp = json.loads(param)

        if "data" not in resp:
            self._setSdkError("解析失败,不存在的data")
            return None

        if resp["data"]["emsg"] is not "":
            self._setRequestError(resp["data"]["emsg"])
            return None

        if "data" not in resp["data"]:
            return None

        return resp["data"]["data"]

    def _getUrl(self, method):
        pass
