# 第 2 天第 1 题：奶茶版 2.0（三个数字全部由你输入，代码里不写死）

# 1) 问「你有多少钱」，接进 money 盒子
money = input("你有多少钱?")
# 2) 原地升级：把文字变成数字（凡是参与算术的盒子都要这步）
money = int(money)

# 3) 问「每杯多少钱」，接进 price 盒子
price = input("每杯多少钱?")
# 4) 原地升级
price = int(price)

# 5) 问「买几杯」，接进 cups 盒子
cups = input("买几杯?")
# 6) 原地升级
cups = int(cups)

# 7) 算花了多少 = 单价 × 杯数，接进 total
total = price * cups
# 8) 算还剩多少 = 你有多少钱 - 花了多少，接进 left
left = money - total

# 9) 打印结果（引号里是给人看的字，逗号后面是不带引号的盒子）
print("花了多少:", total)
print("还剩多少:", left)

# 第 2 天第 2 题：两个数做三件事（和、差、积）
# 套路跟第 1 题一模一样：两个 input 各自接盒子、各自 int、然后三行算术

a = input("第一个数?")
a = int(a)

b = input("第二个数?")
b = int(b)

he = a + b      # 和
cha = a - b     # 差
ji = a * b      # 积

print("和:", he)
print("差:", cha)
print("积:", ji)
