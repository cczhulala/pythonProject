# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 17:36
'''
upper() 所有都转大写  会产生新字符串对象
lower() 所有都转小写  会产生新对象，即使原来是小写的
swapcase() 大写转小写，小写转大写
capitalize() 第一个转大写，其余小写
title()把每个单词的第一个转大写，剩余字符转小写
'''
s = 'hello,hello'
a = s.upper()
print(a,id(a))
print(s,id(s))