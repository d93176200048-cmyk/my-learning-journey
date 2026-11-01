"""
模拟合约2.py
演示 StoreNumber2 的"门禁"：只有部署者（owner）能改数字，别人调 store 会被拒。
接回上次学的：私钥 = 控制权 → Not your keys, not your coins
"""
import json

with open("StoreNumber2_sol_StoreNumber2.bin", "r") as f:
    合约代码 = f.read()
with open("StoreNumber2_sol_StoreNumber2.abi", "r") as f:
    合约接口 = json.load(f)

print("=== 第一步：编译产物就绪 ===")
for 项 in 合约接口:
    if 项.get("type") == "function":
        print("  -", 项["name"], "()", "（参数:", 项.get("inputs"), "返回:", 项.get("outputs"), "）")

# 链上状态
链上状态 = {"myNumber": 0, "owner": None}

def 调用(函数名, 调用者地址, *参数):
    """模拟以太坊调用。调用者地址 = msg.sender"""
    if 函数名 == "retrieve":
        return 链上状态["myNumber"]
    if 函数名 == "whoIsOwner":
        return 链上状态["owner"]
    if 函数名 == "store":
        if 调用者地址 != 链上状态["owner"]:
            raise Exception("你不是主人，无权改数字")  # require 失败的效果
        链上状态["myNumber"] = 参数[0]
        print(f"  [store] 主人把数字改成 {参数[0]}，gas 费 -0.0003 ETH")
        return None
    raise Exception("未知函数: " + 函数名)

print("\n=== 第二步：部署合约 ===")
主人地址 = "0xAbC123"  # 模拟部署者（他手里的私钥 = 控制权）
链上状态["owner"] = 主人地址
print("合约已部署。owner（主人）= ", 主人地址)

print('\n=== 第三步：问"谁是主人" ===')
print("whoIsOwner() 返回:", 调用("whoIsOwner", 主人地址))

print("\n=== 第四步：主人调用 store(42) ===")
调用("store", 主人地址, 42)

print("\n=== 第五步：retrieve() ===")
print("retrieve() 返回:", 调用("retrieve", 主人地址))

print("\n=== 第六步：陌生人（0xEvil）也想调用 store(99) ===")
try:
    调用("store", "0xEvil", 99)
    print("❌ 陌生人居然改成功了 —— 门禁失效")
except Exception as e:
    print("✅ 被拒了:", e)

print("\n=== 第七步：再 retrieve，数字应该还是 42（没被改成 99）===")
print("retrieve() 返回:", 调用("retrieve", 主人地址))

print("\n=== 结论 ===")
if 链上状态["myNumber"] == 42:
    print("✅ 门禁生效：只有主人能改，陌生人被 require 挡住，数字没被篡改")
else:
    print("❌ 出错了")