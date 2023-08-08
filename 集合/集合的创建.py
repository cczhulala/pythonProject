# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 23:59
#集合是可变序列，集合是没有value的字典，也使用{}创建，使用hash创建,也是无序
#1、
s = {'python','world',98,1,2,1}
print(s)#集合与字典一样，不能重复

#2、

s1 = set(range(6))
print(s1,type(s1))

s2 = set([3,4,5,6])
print(s2,type(s2))

s3 = set('hello')
print(s3,type(s3))

s4 = set({123,45,15})
print(s4,type(s4))

s5 = set((3,4,2,5))
print(s5,type(s5))

#定义空集合
s6 = set()
print(type(s6))