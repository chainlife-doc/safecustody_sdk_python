import sys

from safecustody_sdk.request import Request


class RouteController(Request):
    # 路由映射表
    __route = {
        "QueryCoinConf": "coinconf.php",
        "QueryCoins": "info.php",
        "QueryIsInternalAddr": "internal-addr/query.php",
        "ValidateWithdraw": "withdraw/validator.php",
        "QueryBalance": "balance.php",
        "GetDepositHistory": "deposit/history.php",
        "SubmitWithdraw": "withdraw/submit.php",
        "QueryWithdrawStatus": "withdraw/status.php",
        "GetDepositAddr": "deposit/addr.php",
        "QueryWithdrawHistory": "withdraw/history.php",
    }

    # 单个币种查询
    def QueryCoinConf(self, coin):
        metohd = sys._getframe().f_code.co_name
        p = {"coin": coin}
        return self._request(metohd, p)

    # 查询币种公共信息
    def QueryCoins(self):
        metohd = sys._getframe().f_code.co_name
        return self._request(metohd, None)

    # 查询余额
    def QueryBalance(self, param: list):
        metohd = sys._getframe().f_code.co_name
        p = {"coins": param}
        return self._request(metohd, p)

    # 获取充值地址
    def GetDepositAddr(self, param: list):
        metohd = sys._getframe().f_code.co_name
        p = {"coins": param}
        return self._request(metohd, p)

    # 获取充值记录
    def GetDepositHistory(self, subuserId, chain, coin, fromId=0, limit=100):
        metohd = sys._getframe().f_code.co_name
        p = {
            "subuserid": subuserId,
            "chain": chain,
            "coin": coin,
            "fromid": fromId,
            "limit": limit,
        }
        return self._request(metohd, p)

    # 内部地址查询
    def QueryIsInternalAddr(self, coin, chain, addr):
        metohd = sys._getframe().f_code.co_name
        p = {
            "chain": chain,
            "coin": coin,
            "addr": addr
        }
        r, err = self._request(metohd, p)
        if r is None and r is "":
            return False, err
        if (err is not None) and (err is not ""):
            return False, err
        if r["exist"] is 0:
            return False, None
        return True, None

    # 提交提币工单
    def SubmitWithdraw(self, subuserid, chain, coin, addr, amount, memo="", usertags=""):
        metohd = sys._getframe().f_code.co_name
        p = {
            "subuserid": subuserid,
            "chain": chain,
            "coin": coin,
            "addr": addr,
            "amount": amount,
            "memo": memo,
            "usertags": usertags,
            "sign": self._user.getSign(addr, memo, usertags),
        }

        return self._request(metohd, p)

    # 提币预校验接口
    def ValidateWithdraw(self, subuserid, chain, coin, addr, amount, memo="", usertags=""):
        metohd = sys._getframe().f_code.co_name
        p = {
            "subuserid": subuserid,
            "chain": chain,
            "coin": coin,
            "addr": addr,
            "amount": amount,
            "memo": memo,
            "usertags": usertags,
            "sign": self._user.getSign(addr, memo, usertags),
        }
        _, err = self._request(metohd, p)
        if err is None or err is "":
            return True, None

        return False, err

    # 查询提币工单状态
    def QueryWithdrawStatus(self, coin, chain, withdrawid):
        metohd = sys._getframe().f_code.co_name
        p = {
            "chain": chain,
            "coin": coin,
            "withdrawid": withdrawid,
        }
        return self._request(metohd, p)

    # 查询提币记录
    def QueryWithdrawHistory(self, subuserId, chain, coin, fromId=0, limit=100):
        metohd = sys._getframe().f_code.co_name
        p = {
            "subuserid": subuserId,
            "chain": chain,
            "coin": coin,
            "fromid": fromId,
            "limit": limit,
        }
        return self._request(metohd, p)

    def _getUrl(self, method):
        if len(self._host) == 0:
            self._setSdkError("没有设置host")
            return None
        if self._host[-1] != "/":
            self._host = self._host + "/"

        if (method in self.__route) is True:
            method = self.__route[method]

        url = self._host + method

        return url
