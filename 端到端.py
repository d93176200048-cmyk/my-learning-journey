import requests  
import hashlib
地址="https://ethereum-rpc.publicnode.com"
问={
    "jsonrpc":"2.0",
    "method":"eth_getBlockByNumber",
    "params":["latest",True],
    "id":1
}
回=requests.post(地址,json=问,timeout=20)
区块=回.json()["result"]
区块高度=int(区块["number"],16)
print("区块高度:",区块高度)
print("这个区块有几笔交易:",len(区块["transactions"]))
第一笔交易=区块["transactions"][0]
交易哈希=第一笔交易["hash"]
问2={
     "jsonrpc":"2.0",
     "method":"eth_getTransactionReceipt",
     "params":[交易哈希],
     "id":1
}
回2= requests.post(地址,json=问2,timeout=20)
收据=回2.json()["result"]
print("成功了没有:",收据["status"])
print("烧了多少油:",int(收据["gasUsed"],16))
print("留了几条记录:",len(收据["logs"]))
发起方=第一笔交易["from"]
接收方=第一笔交易["to"]
print("发起方地址:",发起方)
def 问节点(要问什么, 查哪个地址):
    交易明细={
        "jsonrpc":"2.0",
        "method": 要问什么,
        "params": [查哪个地址,"latest"],
        "id":1
    }
    回信=requests.post(地址,json=交易明细,timeout=20)
    return 回信.json()["result"]
发起方余额=问节点("eth_getBalance",发起方)
接收方余额=问节点("eth_getBalance",接收方)
发起方代码=问节点("eth_getCode",发起方)
接收方代码=问节点("eth_getCode",接收方)
print("余额(wei):",发起方余额)
print("余额ETH:",int(发起方余额,16)/10**18)
if 发起方代码=="0x":
    print("发起方是:个人账户")
else :
    print("合约账号")
if 接收方代码=="0x":
   print("接收方是:个人账号")
else :
    print("接收方是:合约账号")
账本=open("交易账本.txt","a",encoding="utf-8")
一行=f"{区块高度}|{交易哈希}|{发起方}|{接收方}|{收据['status']}|{int(收据['gasUsed'],16)}"
账本.write(一行+"\n")
账本.close()
账本内容=open("交易账本.txt","r",encoding="utf-8").read()
指纹=hashlib.sha256(账本内容.encode("utf-8")).hexdigest()
print("整个账本的指纹:",指纹)