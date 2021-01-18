from safecustody_sdk.sdk import Sdk
from safecustody_sdk.user import User

# 使用sdk任何签名不需要自己实现,内部已经做好
# 这里只是举的例子,更多详细内容请阅读文档

user = User()

# 对应商户后台的APPID
user.setAppid("")
# 对应商户后的商户id
user.setUserid("")
# 对应商户后台的APIKEY
user.setApiKey("")
# 对应商户后台的SECRETKEY
user.setSecretKey("")

sdk = Sdk(user)
# TODO  请向微信群的官方人员获取
sdk.setHost("")

# 单币种查询
arr, err = sdk.QueryCoinConf("btc")
print(arr)
print(err)

# 查询币种全部信息
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

# 取消提币接口
arr,err = sdk.WithdrawCancel(subuserId="26", chain="trx", coin="trx", withdrawid="")
print(arr)
print(err)

# 查询区块高度
arr,err = sdk.BlockHeight(coin="btc", chain="btc")
print(arr)
print(err)
