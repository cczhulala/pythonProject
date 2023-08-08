# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 23:26
#编码，将字符串转化为二进制数据(bytes)
#解码，将bytes转化为字符串类型

s = '天涯共此时'
print(s.encode(encoding = 'GBK'))#GDK中一个中文占两个字节
print(s.encode(encoding = 'UTF-8'))#占三个

#解码,byte代表就是一个二进制数据
byte = s.encode(encoding ='GBK') #编码 注意encoding不能加s
print(byte.decode(encoding = 'GBK')) #解码  编码和解码格式要相同