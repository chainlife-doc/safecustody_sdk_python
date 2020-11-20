from safecustody_sdk.sdk import Sdk
from safecustody_sdk.user import User

user = User()

user.setAppid("")
user.setUserid("26")
user.setSalt(
    "")

sdk = Sdk(user)
sdk.setHost("")

# 单币种查询
arr, err = sdk.QueryCoinConf("btc")
print(arr)
print(err)

# 查询币种公共信息
arr, err = sdk.QueryCoins()
print(arr)
print(err)

# 查询余额
arr, err = sdk.QueryBalance([{"chain": "eth", "coin": "usdt"}])
print(arr)
print(err)

# 获取充值地址
arr, err = sdk.GetDepositAddr([{"chain": "trx", "coin": "trx", "subuserid": "1"}])
print(arr)
print(err)

# 获取充值记录
arr, err = sdk.GetDepositHistory(subuserId="", chain="trx", coin="trx", fromId=0, limit=100)
print(arr)
print(err)

# 内部地址查询
arr, err = sdk.QueryIsInternalAddr(coin="trx", chain="trx", addr="")
print(arr)
print(err)

# 提交提币工单
arr, err = sdk.SubmitWithdraw(subuserid="", chain="", coin="", addr="", amount="", memo="", usertags="")
print(arr)
print(err)

# 提币预校验接口
arr, err = sdk.ValidateWithdraw(subuserid="", chain="", coin="", addr="", amount="", memo="", usertags="")
print(arr)
print(err)

# 查询提币工单状态
arr, err = sdk.QueryWithdrawStatus(coin="", chain="", withdrawid="")
print(arr)
print(err)

# 查询提币记录
arr, err = sdk.QueryWithdrawHistory(subuserId="26", chain="trx", coin="trx", fromId=0, limit=100)
print(arr)
print(err)
