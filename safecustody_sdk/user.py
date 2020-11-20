import time
import hashlib


# 用户信息类
class User:
    # 用户id
    __userid = ""

    # appid
    __appid = ""

    # salt
    __salt = ""

    # 时间戳
    __time = ""

    # 设置用户id
    def setUserid(self, useid):
        self.__userid = useid

    # 获取用户id
    def getUserId(self):
        return self.__userid

    # 设置appid
    def setAppid(self, appid):
        self.__appid = appid

    # 获取appid
    def getAppid(self):
        return self.__appid

    # 设置salt
    def setSalt(self, salt):
        self.__salt = salt

    # 获取salt
    def getSalt(self):
        return self.__salt

    # 获取用户验证时间
    def getTime(self):
        if self.__time is None or self.__time is "" or self.__time is 0:
            self.__time = int(time.time())
        return str(self.__time)

    # 获取token
    def getAuth(self):
        tokenStr = self.__appid + "_" + self.__salt + "_" + self.__userid + "_" + self.getTime()
        return hashlib.md5(tokenStr.encode("utf-8")).hexdigest()

    # 获取签名
    def getSign(self, addr, memo="", usertags=""):
        signStr = self.__appid + "_" + self.__salt + "_" + self.__userid + "_" + self.getTime() + "_" + addr + "_" + memo + "_" + usertags
        return hashlib.md5(signStr.encode("utf-8")).hexdigest()

    def unsetTime(self):
        self.__time = None
