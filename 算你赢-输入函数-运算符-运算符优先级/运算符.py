# 编写人 : 陈昌志
# 开发时间 : 2022/7/25 15:35
#  //整除运算       %取余   **幂运算
print(9//4)
print(9//-4)
print(9%4)
print(9%-4)

#赋值运算符
a=b=c=10#链式赋值，abc标识id都相同
a+=10#参数赋值
a,b,c = 10,20,30#系列解包赋值
print(type(a))

#交换数值
a,b = b,a

#运算符
print('a>b?',a>b)
'''==比较的是值， is比较的是标识，is not'''
a = 10
b = 10
print(a is b)#True，标识相等

'''布尔运算符  and or not in not in'''
s = 'abc'
print('a' in s)
print('a' not in s)

#位运算符& | ^ ~ << >>
a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b  # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b  # 61 = 0011 1101
print("2 - c 的值为：", c)

c = a ^ b  # 49 = 0011 0001
print("3 - c 的值为：", c)

c = ~a  # -61 = 1100 0011
print("4 - c 的值为：", c)

c = a << 2  # 240 = 1111 0000    相当于乘以4
print("5 - c 的值为：", c)

c = a >> 2  # 15 = 0000 1111    相当于除以4
print("6 - c 的值为：", c)
