# 复核.py —— 演示：重新算指纹，跟文件里存的旧指纹比，看笔记有没有被改过
import hashlib

文件 = open("tamper_demo.txt", "r", encoding="utf-8")
行们 = 文件.read().splitlines()
文件.close()

for 行 in 行们:
    行 = 行.strip()
    if 行.count(":") < 2:        # 跳过没有两道英文冒号的行
        continue
    标题, 内容, 旧指纹 = 行.rsplit(":", 2)   # 从右边切两刀：标题 / 内容 / 指纹
    重算 = hashlib.sha256(内容.encode("utf-8")).hexdigest()
    if 重算 == 旧指纹:
        print(标题, "→ 没动过 ✓")
    else:
        print(标题, "→ 被改过 ✗")
