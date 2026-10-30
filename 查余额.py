import requests

地址 = "https://ethereum-rpc.publicnode.com"

# ↓↓↓ 下面 4 段照抄你 抓交易.py 的前半段 ↓↓↓
问 = {
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": ["latest", True],
    "id": 1
}
回 = requests.post(地址, json=问, timeout=20)
区块 = 回.json()["result"]
第一笔 = 区块["transactions"][0]

# ↓↓↓【新】拿到这笔交易的发起方地址 ↓↓↓
发起方 = 第一笔["from"]
print("发起方地址:", 发起方)

# ↓↓↓【新】查这个地址的余额 ↓↓↓
问2 = {
    "jsonrpc": "2.0",
    "method": "eth_getBalance",        # 【新】方法名：查余额
    "params": [发起方, "latest"],        # 【新】要传：地址 + 查哪个时刻(latest=现在)
    "id": 1
}
回2 = requests.post(地址, json=问2, timeout=20)
余额wei = 回2.json()["result"]
print("余额(wei):", 余额wei)
print("余额(ETH):", int(余额wei, 16) / 10**18)   # 老朋友：wei→ETH 换算
