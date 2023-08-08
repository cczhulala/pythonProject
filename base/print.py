# 编写人 : 陈昌志
# 开发时间 : 2022/7/24 16:23

#print 可以输出字符，数字，运算式，输出文件，屏幕，还可以换行输出

print(50)

print(50+1)

print("  11")
print('11')

fp = open('text.txt','a+')   #写入记得要file=，并且路径名要写正确
print("hello world",file=fp)   #https://wenku.baidu.com/view/2611a4a1bfeb19e8b8f67c1cfad6195f312be8be.html
fp.close()


#不进行换行输出
print('hello','python')
