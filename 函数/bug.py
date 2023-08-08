# 编写人 : 陈昌志
# 开发时间 : 2022/7/29 13:35
'''
异常处理机制
可以在出现异常时捕获，内部消化，让程序继续运行
try:
可能出问题的代码
except xxx:   xxx是异常类型
异常处理代码
'''
try:
    n1 = int(input('请输入第一个数字'))
    n2 = int(input('2'))
    result = n1/n2
    print('结果为：',result)
except ZeroDivisionError:    #从上到下，最后base是最基础的错误，是父类，前面是子类
    print('除数不允许为0')
except ValueError:
    print('cuo')
except BaseException as e:
    print(e)
print('程序结束')
