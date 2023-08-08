# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 17:31
'''
index()，查找子串第一次出现的位置，不存在报错
rindex()  查找最后一次出现的位置，不存在报错
find()  第一次出现，不存在返回-1
rfind()  最后一次出现，不存在-1
'''

s = 'hello,hello'
print(s.index('lo'))#3
print(s.find('lo'))#3
print(s.rindex('lo'))#9
print(s.rfind('lo'))#9