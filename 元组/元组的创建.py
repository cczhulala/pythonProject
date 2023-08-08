# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 23:33
#元组是不可变的序列，没有增删改，//字符串
#可变序列执行完增删改，对象地址不发生变化

lst = [10,20,30]
print(id(lst))
lst.append(40)
print(id(lst))

'''不可变序列'''
s = 'hello'
s = s +'world'
print(id(s))
print(s)

#元组的创建
#1
t = ('python',98)
print(t)
print(type(t))

t2 = 'python',85#第一种创建方式可以缩略小括号
t3 = ('python',)#只包含一个元素需要括号加上逗号，
# 如果没有逗号，那么系统认为这是一个字符串，str类型，而不是tuple类型

#2、
t1 = tuple(('py',98))
print(t)
print(type(t1))

#空元组,空列表，空字典
lst=[]
lst1=list()

d={}
d2 = dict()

t4=()
t5 = tuple()

