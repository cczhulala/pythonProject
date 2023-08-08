# 编写人 : 陈昌志
# 开发时间 : 2022/7/24 16:37
#coding:utf-8
#  \反斜杠是转义字符 \\  \'   \"

#  \n换行  \r回车  \t水平制表符  \b退格   一个制表位有4个  hello=4+1，加制表符只有3个空
#
'''

'''
print('hello\nworld')
print('hello\bworld')
print('hello\rworld') #覆盖了hello

#原字符，不希望转义字符起作用，在字符串之前加上r，或者R
print(r'hello\nworld')#print(r'hello\nworld\')是错误的，如果最后是\\那么这是正确的