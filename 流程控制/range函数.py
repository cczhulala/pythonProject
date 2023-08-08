# 编写人 : 陈昌志
# 开发时间 : 2022/7/25 22:31
#三种创建方式
#1
r = range(10)
print(r)#这个不能查看r中的数字
print(list(r))#list是列表的意思，用于查看range中的整数序列
print(type(r))
#2
b = range(5,10)#从5开始，不包含10，因为宇宙无限，默认步长为1
print(list(b))

#3
c = range(5,15,2)#最后一个是步长
print(list(c))

#判断数是否在序列中存在 in； not in
print(5 in c)