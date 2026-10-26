import hashlib
学习=open("学习哈希.txt","w")
学习.write("体验ai和web3\n")
学习.close()
学习=open("学习哈希.txt","r")
内容=学习.read()
print(内容)
文字="体验ai和web3"
字节=文字.encode("utf-8")
指纹 = hashlib.sha256(字节).hexdigest()
print(文字)
print(指纹)
文字2="体验ai和web3!"
指纹2=hashlib.sha256(文字2.encode("utf-8")).hexdigest()
print(文字2)
print(指纹2)
print(指纹==指纹2)
