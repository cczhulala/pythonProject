# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 23:26
#使用内置函数zip()，将可迭代的对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
item=['a','b','c']
price=[100,200,300]
lst = zip(item,price)
print(lst)
print(list(lst))#返回的是列表

#字典生成式{}
d = {item.upper():price for item,price in zip(item,price)}#upper是把字母变成大写
print(d)#如果两个不一样长，那么只会输出比较短的