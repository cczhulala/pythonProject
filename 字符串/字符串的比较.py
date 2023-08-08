# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 22:59
#使用>,>= == !=等，从第一个字符开始依次比较下去，
# 直到不相等时，比较结果就是两个字符串比较结果，后续不再比较
#比较原理，两个字符进行比较，比较的是其ordinal value值（原始值），
# 调用内置函数ord可以得到指定字符的ordinal value，与内置函数ord对应的是内置函数chr，
# 调用chr时指定ordinal value可以得到其对应字符

print('apple'>'app')
print('apple'>'banana')
print(ord('a'),ord('b'))
print(chr(97),chr(98))