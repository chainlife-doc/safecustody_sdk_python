# 赛福托管钱包API Python-SDK  

## Python version >= 3.0  
### 安装SDK

#### pip安装

- `pip install safecustody_sdk`


#### 源码安装 
    
- 直接从GitHup下载源码,把整个`safecustody_sdk`包放入您的项目目录中,  
  然后在代码里引入:
     ```python
      from safecustody_sdk.sdk import Sdk
      from safecustody_sdk.user import User
    ```
- 安装依赖
    ```python
    pip install -r requirements.txt
    ```       
# 例子

#### 创建sdkApi
 ```python
from safecustody_sdk.sdk import Sdk
from safecustody_sdk.user import User

user = User()

user.setAppid("")
user.setUserid("")
user.setSalt("")

sdk = Sdk(user)
sdk.setHost("")
``` 

#### [单个币种查询](https://github.com/chainlife-doc/wallet-api/blob/master/%E5%8D%95%E5%B8%81%E7%A7%8D%E4%BF%A1%E6%81%AF%E6%9F%A5%E8%AF%A2.md)
```python
# 传入查询的币名
arr, err = sdk.QueryCoinConf("btc")
```

#### [查询公共币种信息](https://github.com/chainlife-doc/wallet-api/blob/master/%E6%9F%A5%E8%AF%A2%E5%B8%81%E7%A7%8D%E4%BF%A1%E6%81%AF.md)
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
# memo 提币备注,内容自定义（会记录到区块链上）      
# usertags 提币标签，内容自定义 （不会记录到区块链上）
arr,err = sdk.SubmitWithdraw(subuserid="", chain="", coin="", addr="", amount="", memo="", usertags="")
```

#### [提币预校验](https://github.com/chainlife-doc/wallet-api/blob/master/withdraw/%E6%8F%90%E5%B8%81%E9%A2%84%E6%A0%A1%E9%AA%8C%E6%8E%A5%E5%8F%A3.md)
```python
# string coin 币名                         
# string chain 链名                        
# string subuserid 你的用户id              
# string addr 提币地址                       
# string amount 提币数量                     
# string memo 提币备注,内容自定义（会记录到区块链上）       
# string usertags 提币标签，内容自定义 （不会记录到区块链上） 
arr,err = sdk.ValidateWithdraw(subuserid="", chain="", coin="", addr="", amount="", memo="", usertags="")
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