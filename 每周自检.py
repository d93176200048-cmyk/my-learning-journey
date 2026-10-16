"""
每周自检脚本（Weekly Self-Check）

用法：在这个文件夹里打开 PowerShell，输入
    python 每周自检.py

作用：自动检查你这周学了什么、离 G1 闸门还差多少。
不用你自己数提交、翻文件——跑一次，全出来。

作者：我自己（第 1 周写的第一个"工具"）
"""

import subprocess   # subprocess：让 Python 能调用外面的命令（这里是 git）
import glob         # glob：按文件名模式找文件，比如找出所有 .py
from datetime import date

# ============================================
# 一个小工具：执行命令并把输出拿回来
# ============================================
def run(cmd):
    """执行一条命令，返回它的文字输出。

    cmd 是一个列表，例如 ["git", "log"] 就是执行 git log 这条命令。
    用列表而不是一串文字，是为了避免路径里有空格出问题。
    """
    result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
    return result.stdout.strip()

# ============================================
# 1. 数一下一共提交了多少次
# ============================================
log_text = run(["git", "log", "--oneline"])
# git log --oneline 每次提交输出一行，按换行切开再数
commits = [line for line in log_text.split("\n") if line.strip()]

# ============================================
# 2. 最近一次提交是哪一天（用来看有没有掉队）
# ============================================
last_day = run(["git", "log", "-1", "--format=%cd", "--date=short"])
days_since = "算不出来"
if last_day:
    y, m, d = last_day.split("-")                 # "2026-10-15" 切成三段
    days_since = (date.today() - date(int(y), int(m), int(d))).days

# ============================================
# 3. 数一下有几个 Python 脚本（G1 要求 ≥15 个）
# ============================================
py_files = glob.glob("*.py")                       # 当前文件夹下所有 .py

# ============================================
# 4. 看 GitHub 远程配了没有（G1 要求已推送）
# ============================================
remote = run(["git", "remote", "-v"])
has_remote = "有" if remote else "没有"

# ============================================
# 输出报告
# ============================================
print("=" * 46)
print("           每 周 自 检 报 告")
print("=" * 46)

print(f"\n[1] 提交总数：{len(commits)} 次")
print(f"[2] 最近一次提交：{last_day or '还没有'}（{days_since} 天前）")
print(f"[3] Python 脚本：{len(py_files)} 个  {py_files}")
print(f"[4] GitHub 远程：{has_remote}")

print("\n" + "-" * 46)
print("G1 闸门完成度（第 6 周末要过）")
print("-" * 46)

# G1 四项，逐项打勾或打叉
items = [
    ("Python 脚本 ≥15 个", len(py_files) >= 15, f"现在 {len(py_files)} 个"),
    ("GitHub 已配置远程并推送", bool(remote), f"现在：{has_remote}"),
    ("能写 200 行以内能跑的程序", None, "这项要你自己判断"),
    ("抓 API → 存 CSV → 出图 小工具", None, "第 3–4 周做"),
]
for name, ok, note in items:
    if ok is True:
        mark = "[v]"
    elif ok is False:
        mark = "[ ]"
    else:
        mark = "[?]"
    print(f"  {mark} {name}    （{note}）")

# ============================================
# 给出「今天只做这一件事」
# ============================================
print("\n" + "=" * 46)
print("今天只做这一件事")
print("=" * 46)

if not remote:
    todo = "把 GitHub 仓库建好并推送（这是唯一卡死 G1 的事）"
elif days_since != "算不出来" and days_since >= 7:
    todo = f"你已经 {days_since} 天没提交了。今天只写一个 10 行的小脚本，提交掉"
elif len(py_files) < 15:
    todo = f"再写 1 个脚本（现在 {len(py_files)}/15），做完就提交"
else:
    todo = "G1 的硬指标已过。今天推进第 3 周：调一个公开 API 取数据存 CSV"

print(f"\n  --> {todo}\n")
