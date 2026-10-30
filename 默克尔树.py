import hashlib

# 假设一个区块里装了 4 笔交易（用文字代替，实际是交易数据）
交易们 = ["小明转给小红 100 ETH", "小刚转给小美 2 ETH", "阿强转给阿珍 0.5 ETH", "老李转给老王 3 ETH"]

# 第 1 层：每笔交易算一个指纹（叫「叶子」）
指纹们 = []
for 交易 in 交易们:
    指纹 = hashlib.sha256(交易.encode("utf-8")).hexdigest()
    指纹们.append(指纹)

print("4 个叶子的指纹：")
for i, 指纹 in enumerate(指纹们):
    print(i, 指纹[:16], "...")

# 第 2 层：两两拼起来再哈希
左 = hashlib.sha256((指纹们[0] + 指纹们[1]).encode("utf-8")).hexdigest()
右 = hashlib.sha256((指纹们[2] + 指纹们[3]).encode("utf-8")).hexdigest()

# 第 3 层（树根）：左右再拼起来哈希一次
根 = hashlib.sha256((左 + 右).encode("utf-8")).hexdigest()

print()
print("左半边组合指纹:", 左[:16], "...")
print("右半边组合指纹:", 右[:16], "...")
print("★ 默克尔树根（整棵树的指纹）:", 根)
