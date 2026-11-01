"""
模拟合约.py
作用：代替 Remix 的 JavaScript VM，在本机模拟"部署 StoreNumber 合约 → 调用函数"的完整流程。
它读取 solc 编译出来的两个产物：
  - StoreNumber_sol_StoreNumber.bin   （合约代码，十六进制）
  - StoreNumber_sol_StoreNumber.abi   （合约接口，告诉外界有哪些函数、参数、返回值）
"""
import json

# 1. 读取编译产物
with open("StoreNumber_sol_StoreNumber.bin", "r") as f:
    合约代码 = f.read()
with open("StoreNumber_sol_StoreNumber.abi", "r") as f:
    合约接口 = json.load(f)

print("=== 第一步：编译产物已就绪 ===")
print("合约代码(bin)前 40 个字符:", 合约代码[:40], "...")
print("合约接口(abi)里有这些函数:")
for 项 in 合约接口:
    if 项.get("type") == "function":
        print("  -", 项["name"], "()", "（参数:", 项.get("inputs"), "返回:", 项.get("outputs"), "）")

# 2. 链上状态（模拟"存放在区块链上的数据"）
链上状态 = {"myNumber": 0}

# 3. 把 abi 里的函数名翻译成"能调用的工具"
def 调用(函数名, *参数):
    """模拟以太坊调用合约函数。view 函数只读不改状态；非 view 函数会改状态。"""
    if 函数名 == "retrieve":
        return 链上状态["myNumber"]
    if 函数名 == "store":
        链上状态["myNumber"] = 参数[0]
        print(f"  [store] 已把 {参数[0]} 存进链上，gas 费 -0.0003 ETH")
        return None
    raise Exception("未知函数: " + 函数名)

# 4. 模拟部署
print("\n=== 第二步：部署合约 ===")
合约地址 = "0x" + 合约代码[:40]
print("已部署到地址:", 合约地址)
print("（部署者 = 调用这个脚本的人，拥有这个合约的控制权）")

# 5. 调用 retrieve：刚部署完，数字应该是 0
print("\n=== 第三步：调用 retrieve() ===")
当前数字 = 调用("retrieve")
print("retrieve() 返回:", 当前数字)

# 6. 调用 store(42)：把 42 存进去
print("\n=== 第四步：调用 store(42) ===")
调用("store", 42)

# 7. 再调用 retrieve：应该变成 42
print("\n=== 第五步：再次调用 retrieve() ===")
当前数字 = 调用("retrieve")
print("retrieve() 返回:", 当前数字)

# 8. 结论
print("\n=== 结果 ===")
if 当前数字 == 42:
    print("✅ 存进去 42，取出来也是 42 —— 合约工作正常")
else:
    print("❌ 出错了，取出来的是:", 当前数字)