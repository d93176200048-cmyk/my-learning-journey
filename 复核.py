import hashlib
笔记本=open("我的笔记.txt","r",encoding="utf-8")
所有行=笔记本.read().splitlines()
笔记本.close()
for 行 in 所有行:
    if 行.count(":")<2:
        continue
    标题,正文,旧指纹=行.split(":")
    指纹2= hashlib.sha256(正文.encode("utf-8")).hexdigest()
    if 指纹2==旧指纹:
        print("没动")
    else:
        print("动了")
 