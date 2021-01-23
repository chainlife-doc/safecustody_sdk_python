# 时代安全钱包API Python-SDK  

## Python version >= 3.0  
### 安装SDK

#### pip安装

- `pip install safecustody_sdk`
    
# 例子

#### 创建sdkApi
 ```python
from safecustody_sdk.sdk import Sdk
from safecustody_sdk.user import User

user = User()

# 对应商户后台的APPID
user.setAppid("")
# 对应商户后的商户id
user.setUserid("")
# 对应商户后台的APIKEY
user.setApiKey("")
# 对应商户后台的SECRETKEY
user.setSecretKey(
    "")

sdk = Sdk(user)

# TODO  请向微信群的官方人员获取
sdk.setHost("")
``` 

#### [单个币种查询](https://github.com/chainlife-doc/wallet-api/blob/master/%E5%8D%95%E5%B8%81%E7%A7%8D%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2.md)
```python
# 传入查询的币名
arr, err = sdk.QueryCoinConf("btc")
```

#### [查询全部币种信息](https://github.com/chainlife-doc/wallet-api/blob/master/%E6%9F%A5%E8%AF%A2%E5%B8%81%E7%A7%8D%E4%BF%A1%E6%81%AF.md)
```python
arr, err = sdk.GetDepositAddr([{"chain": "trx", "coin": "trx", "subuserid": "1"}])
```

#### [查询余额](https://github.com/chainlife-doc/wallet-api/blob/master/%E6%9F%A5%E8%AF%A2%E4%BD%99%E9%A2%9D.md)
```python
# string coin 币名
# string chain 链名
arr, err = sdk.QueryBalance([{"chain": "eth", "coin": "usdt"}])
```

#### [获取充值地址](https://github.com/chainlife-doc/wallet-api/blob/master/deposit/%E8%8E%B7%E5%8F%96%E5%85%85%E5%80%BC%E5%9C%B0%E5%9D%80.md)
```python
# string coin 币名           
# string chain 链名          
# string subuserid 你的用户id
arr, err = sdk.GetDepositHistory(subuserId="", chain="", coin="", fromId=0, limit=100)
```

#### [获取充值记录](https://github.com/chainlife-doc/wallet-api/blob/master/deposit/%E8%8E%B7%E5%8F%96%E5%85%85%E5%80%BC%E8%AE%B0%E5%BD%95.md)
```python
# string coin 币名                                        
# string chain 链名                                       
# string subuserid 你的用户id                               
# int fromid 从哪个充值序号开始，值大于等于1,查询结果包含fromId对应的充值记录       
# int limit 最多查询多少条记录，包含fromid这条记录                      
arr, err = sdk.GetDepositHistory(subuserId="", chain="", coin="", fromId=0, limit=100)
```

#### [内部地址查询](https://github.com/chainlife-doc/wallet-api/blob/master/internal-addr/%E5%86%85%E9%83%A8%E5%9C%B0%E5%9D%80%E6%9F%A5%E8%AF%A2.md)
```python
# string coin 币名      
# string chain 链名     
# string addr 要查询的内部地址
arr,err = sdk.QueryIsInternalAddr(coin="", chain="", addr="")
```

#### [提交提币工单](https://github.com/chainlife-doc/wallet-api/blob/master/withdraw/%E6%8F%90%E4%BA%A4%E6%8F%90%E5%B8%81%E5%B7%A5%E5%8D%95.md)
```python
# coin 币名                        
# chain 链名                       
# subuserid 你的用户id             
# addr 提币地址                      
# amount 提币数量                    
# memo 该字段主要提供给链上支持备注的币种，内容会更新到链上       
# usertags 用户标签, 自定义内容，一般作为订单备注使用,辅助说明
# user_orderid 用户自定义订单ID，该字段主要是填写用户系统的订单流水号，字段具有唯一性（可选字段)
arr,err = sdk.SubmitWithdraw(subuserid="", chain="", coin="", addr="", amount="", memo="", usertags="",user_orderid="")
```

#### [提币预校验](https://github.com/chainlife-doc/wallet-api/blob/master/withdraw/%E6%8F%90%E5%B8%81%E9%A2%84%E6%A0%A1%E9%AA%8C%E6%8E%A5%E5%8F%A3.md)
```python
# string coin 币名                         
# string chain 链名                        
# string subuserid 你的用户id              
# string addr 提币地址                       
# string amount 提币数量                     
# string memo 该字段主要提供给链上支持备注的币种，内容会更新到链上       
# string usertags 用户标签, 自定义内容，一般作为订单备注使用,辅助说明 
# user_orderid 用户自定义订单ID，该字段主要是填写用户系统的订单流水号，字段具有唯一性（可选字段)
arr,err = sdk.ValidateWithdraw(subuserid="", chain="", coin="", addr="", amount="", memo="", usertags="",user_orderid="")
```

#### [查询工单状态](https://github.com/chainlife-doc/wallet-api/blob/master/withdraw/%E6%9F%A5%E8%AF%A2%E6%8F%90%E5%B8%81%E5%B7%A5%E5%8D%95%E7%8A%B6%E6%80%81.md)
```python
# string coin 币名          
# string chain 链名         
# string withdrawid 提币订单ID
arr,err = sdk.QueryWithdrawStatus(coin="", chain="", withdrawid="")
```

#### [查询历史提币记录](https://github.com/chainlife-doc/wallet-api/blob/master/withdraw/%E6%9F%A5%E8%AF%A2%E6%8F%90%E5%B8%81%E8%AE%B0%E5%BD%95.md)
```python
# string coin 币名                                           
# string chain 链名                                          
# string subuserid 你的用户id                                 
# int fromid 从哪个充值序号开始，值大于等于1,查询结果包含fromId对应的充值记录          
# int limit 最多查询多少条记录，包含fromid这条记录                         
arr,err = sdk.GetDepositHistory(subuserId="", chain="", coin="", fromId=0, limit=100)
```

#### [取消提币接口](https://github.com/chainlife-doc/wallet-api/blob/master/withdraw/%E5%8F%96%E6%B6%88%E6%8F%90%E5%B8%81%E6%8E%A5%E5%8F%A3.md)
```python
# string coin 币名                                           
# string chain 链名                                          
# string subuserid 你的用户id  
# string withdrawid 提币订单ID
arr,err = sdk.WithdrawCancel(self, subuserId, chain, coin, withdrawid)
```

#### [查询区块高度](https://github.com/chainlife-doc/wallet-api/blob/master/%E6%9F%A5%E8%AF%A2%E5%B8%81%E7%A7%8D%E8%8A%82%E7%82%B9%E9%AB%98%E5%BA%A6.md)
```python
# string coin 币名                                           
# string chain 链名  
arr,err = sdk.BlockHeight(coin="btc", chain="btc")
print(arr)
print(err)
```