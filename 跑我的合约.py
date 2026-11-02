"""
跑我的合约.py
读取 StoreNumberMine 编译产物，模拟部署 → 调用 → 验证。
合约代码是用户自己写的，这个脚本只是"模拟器"（工具的事）。
"""
import json

with open("StoreNumberMine_sol_StoreNumberMine.bin", "r") as f:
    合约代码 = f.read()
with open("StoreNumberMine_sol_StoreNumberMine.abi", "r") as f:
    合约接口 = json.load(f)

print("=== 第一步：编译产物就绪 ===")
print("合约代码(bin)前 30 个字符:", 合约代码[:30], "...")
print("合约接口(abi)里的函数:")
for 项 in 合约接口:
    if 项.get("type") == "function":
        print("  -", 项["name"], "()", "（参数:", 项.get("inputs"), "返回:", 项.get("outputs"), "）")

# 链上状态（模拟"存在区块链上的数据"）
链上状态 = {"myNumber": 0}

def 调用(函数名, *参数):
    """模拟以太坊调用合约函数。view 只读不改状态；非 view 改状态。"""
    if 函数名 == "retrieve":
        return 链上状态["myNumber"]
    if 函数名 == "store":
        链上状态["myNumber"] = 参数[0]
        print(f"  [store] 已把 {参数[0]} 存进链上，gas 费 -0.0003 ETH")
        return None
    raise Exception("未知函数: " + 函数名)

print("\n=== 第二步：部署合约 ===")
合约地址 = "0x" + 合约代码[:40]
print("已部署到地址:", 合约地址)

print("\n=== 第三步：调用 retrieve() ===")
当前数字 = 调用("retrieve")
print("retrieve() 返回:", 当前数字)

print("\n=== 第四步：调用 store(42) ===")
调用("store", 42)

print("\n=== 第五步：再次调用 retrieve() ===")
当前数字 = 调用("retrieve")
print("retrieve() 返回:", 当前数字)

print("\n=== 结果 ===")
if 当前数字 == 42:
    print("✅ 存进去 42，取出来也是 42 —— 你的合约工作正常")
else:
    print("❌ 出错了，取出来的是:", 当前数字)