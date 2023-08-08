# 编写人 : 陈昌志
# 开发时间 : 2022/7/25 22:41
#while循环
i = 1
sum = 0
while i<5:
    sum += i
    i += 1
print(sum)

#for in循环
for item in 'python':
    print(item)
#如果不用到这个变量，可以将自定义变量写为“_”
for _ in range(5):
    print("看看看")

#break  运行完之后执行else之后的内容
for _ in range(3):
    if int(input("请输入密码："))==111:
        print('正确')
        break
    else:
        print('请重新输入密码')
else:print('密码错误太多次')

#continue结束当前循环，进入下一次循环

#else可以和while和for一起使用，但是要是遇见break了，就不会执行

#嵌套循环 + 不换行输出
for i in range(1,10):
    for j in range(1,i+1):
        print(i,'*',j,'=',i*j,end='\t') #不换行输出
    print()#打行

#二层循环中的break和continue只用于本层循环