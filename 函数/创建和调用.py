# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 23:33
'''
def 函数名([输入参数]):
    函数体
    [return xxx]
'''


def calc(a, b):
    c = a + b
    return c


result = calc(10, 20)#位置实参
print(result)

result1 = calc(b=100, a=50)#关键字实参，可以和位置实参混合用
print(result1)

#如果传入可变序列，那么对可变序列的操作，会改变可变序列；
# 传入整数之类的不可变序列，那么不会改变原来的，
# 和C语言不同
#形参和实参名字可以不同
