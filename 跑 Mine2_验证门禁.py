import json

with open("StoreNumberMine2_sol_StoreNumberMine2.bin", "r") as f:
    合约代码 = f.read()
with open("StoreNumberMine2_sol_StoreNumberMine2.abi", "r") as f:
    合约接口 = json.load(f)

print("=== 编译产物就绪 ===")
for 项 in 合约接口:
    if 项.get("type") == "function":
        print("  -", 项["name"], "()")

链上状态 = {"myNumber": 0, "owner": "0xMaster"}

def 调用(函数名, 调用者地址, *参数):
    if 函数名 == "retrieve":
        return 链上状态["myNumber"]
    if 函数名 == "reset":
        if 调用者地址 != 链上状态["owner"]:
            raise Exception("主人调用者")
        链上状态["myNumber"] = 0
        print("  [reset] " + 调用者地址 + " 把数字归零")
        return None
    if 函数名 == "store":
        链上状态["myNumber"] = 链上状态["myNumber"] + 参数[0]
        return None
    raise Exception("未知函数")

print("\n=== 部署合约 ===")
print("owner =", 链上状态["owner"])

print("\n=== 主人 store(42) ===")
调用("store", 链上状态["owner"], 42)
print("retrieve() =", 调用("retrieve", 链上状态["owner"]))

print("\n=== 主人调用 reset() ===")
调用("reset", 链上状态["owner"])
print("retrieve() =", 调用("retrieve", 链上状态["owner"]))

print("\n=== 再来一轮：store(100) ===")
调用("store", 链上状态["owner"], 100)
print("retrieve() =", 调用("retrieve", 链上状态["owner"]))

print("\n=== 陌生人 (0xEvil) 调用 reset() ===")
try:
    调用("reset", "0xEvil")
    print("❌ 陌生人居然归零成功了")
except Exception as e:
    print("✅ 被拒了:", e)

print("\n=== 再 retrieve，数字应该还是 100 ===")
print("retrieve() =", 调用("retrieve", 链上状态["owner"]))

print("\n=== 结论 ===")
if 链上状态["myNumber"] == 100:
    print("✅ 门禁生效：只有主人能 reset，陌生人被挡")
else:
    print("❌ 出错了")