import requests
地址= "https://ethereum-rpc.publicnode.com"
问 ={
    "jsonrpc":"2.0",
    "method":"eth_getBlockByNumber",
    "params":["latest",True],
    "id":1
}
回 = requests.post(地址,json=问,timeout=20)
区块 = 回.json()["result"]
print("区块高度:",int(区块["number"],16))
print("这个区块有几笔交易:",len(区块["transactions"]))
第一笔= 区块["transactions"][0]
print(第一笔["from"])
print(第一笔["to"])
print(第一笔["value"])
print("这笔转了多少ETH:", int(第一笔["value"],16) / 10**18)
print("区块指纹:",区块["hash"])
print("交易哈希:",第一笔["hash"])