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
交易哈希 = 第一笔["hash"]
print("交易哈希:", 交易哈希)

# ↓↓↓【新】用交易哈希去查它的收据 ↓↓↓
问2 = {
    "jsonrpc": "2.0",
    "method": "eth_getTransactionReceipt",     # 【新】方法名：查收据
    "params": [交易哈希],                        # 【新】要传的是交易哈希
    "id": 1
}
回2 = requests.post(地址, json=问2, timeout=20)
收据 = 回2.json()["result"]

print("交易是否成功:", 收据["status"])          # 【新】0x1=成功 0x0=失败
print("实际花了多少 Gas:", int(收据["gasUsed"], 16))   # 【新】实花 Gas
print("产生了几条日志:", len(收据["logs"]))     # 【新】合约留下的记录条数
