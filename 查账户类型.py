import requests

地址 = "https://ethereum-rpc.publicnode.com"

问 = {
    "jsonrpc": "2.0",
    "method": "eth_getBlockByNumber",
    "params": ["latest", True],
    "id": 1
}
回 = requests.post(地址, json=问, timeout=20)
区块 = 回.json()["result"]
第一笔 = 区块["transactions"][0]

发起方 = 第一笔["from"]
接收方 = 第一笔["to"]
print("发起方:", 发起方)
print("接收方:", 接收方)

# 对「发起方」和「接收方」各查一次：它里面有没有存代码
for 角色, 账户 in [("发起方", 发起方), ("接收方", 接收方)]:
    问2 = {
        "jsonrpc": "2.0",
        "method": "eth_getCode",        # 【新】查这个地址里存没存"代码"
        "params": [账户, "latest"],
        "id": 1
    }
    回2 = requests.post(地址, json=问2, timeout=20)
    代码 = 回2.json()["result"]
    if 代码 == "0x":
        print(角色, "= 【人】的账户（EOA），里面没有代码，只有余额")
    else:
        print(角色, "= 【合约】账户，里面存着可执行的代码")
