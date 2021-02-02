import time
import hashlib


# 用户信息类
class User:
    # 对应商户后的商户id
    __userid = ""

    # 对应商户后台的APPID
    __appid = ""

    # 对应商户后台的SECRETKEY
    __secretKey = ""

    # 时间戳
    __time = ""

    # 对应商户后台的APIKEY
    __apiKey = ""

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

    # 设置SECRETKEY
    def setSecretKey(self, secretKey):
        self.__secretKey = secretKey

    # 获取SECRETKEY
    def getSecretKey(self):
        return self.__secretKey

    def setApiKey(self, apiKey):
        self.__apiKey = apiKey

    def getApiKey(self):
        return self.__apiKey

    # 获取用户验证时间
    def getTime(self):
        if self.__time is None or self.__time is "" or self.__time is 0:
            self.__time = int(time.time())
        return str(self.__time)

    # 获取token
    def getAuth(self):
        tokenStr = self.__apiKey + "_" + self.__secretKey + "_" + self.__userid + "_" + self.getTime()
        return hashlib.md5(tokenStr.encode("utf-8")).hexdigest()

    # 获取签名
    def getSign(self, addr, memo="", usertags="", userOrderId=""):

        str = ""
        if userOrderId != "":
            str = "_" + userOrderId

        signStr = self.__apiKey + "_" + self.__secretKey + "_" + self.__userid + "_" + self.getTime() + "_" + addr + "_" + memo + "_" + usertags + \
                  str

        return hashlib.md5(signStr.encode("utf-8")).hexdigest()

    def unsetTime(self):
        self.__time = None
