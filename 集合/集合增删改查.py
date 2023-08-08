# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 0:12
'''
集合的判断用 in not in
增加用add(),一次添加一个，用update()至少添加一个
用remove()一次删除一个指定元素，如果不存在报错
discard()一次删除一个指定元素，不存在不报错
pop()一次删除一个任意元素
clear()清空集合
'''

s={10,20,30,405,60}
print(10 in s)
print(100 not in s)

print('---------------集合的新增--------------')
s.add(80)
print(s)
s.update({200,400,300})
print(s)
s.update([444,555])
print(s)
s.update((999,888,777))
print(s)

print('------------------集合的删除---------------')
s.remove(999)
print(s)
s.discard(200)
print(s)

s.pop()
print(s)

s.clear()
print(s)