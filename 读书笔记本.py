import hashlib
def 收集笔记():
    条数文字=input("要记几条笔记？")
    条数=int(条数文字)
    笔记列表=[]
    计数器=1
    while 计数器 <=条数:
         标题=input("笔记标题:")
         内容=input("笔记内容:")
         字节=内容.encode("utf-8")
         指纹=hashlib.sha256(字节).hexdigest()
         笔记本={"标题":标题,"内容":内容,"指纹":指纹}
         笔记列表.append(笔记本)
         计数器=计数器+1
    return 笔记列表
def 写文件(笔记列表):
    我的笔记本=open("我的笔记.txt","a",encoding="utf-8")
    for 笔记 in 笔记列表:
        内容=笔记["标题"]+":"+笔记["内容"]+":"+笔记["指纹"]+"\n"
        我的笔记本.write(内容)
    我的笔记本.close()
def 读回():
    我的笔记本=open("我的笔记.txt","r",encoding="utf-8")
    内容=我的笔记本.read()
    我的笔记本.close()
    return 内容
def 复核():
    我的笔记本=open("我的笔记.txt","r",encoding="utf-8")
    所有行=我的笔记本.read().splitlines()
    我的笔记本.close()
    for 行 in 所有行:
        if 行.count(":") < 2:
            continue
        标题,正文,旧指纹 = 行.split(":") 
        指纹2=hashlib.sha256(正文.encode("utf-8")).hexdigest()
        if 指纹2 == 旧指纹:
            print("没动")
        else:
            print("动了")
笔记列表=收集笔记()
写文件(笔记列表)
print(读回())
复核()









