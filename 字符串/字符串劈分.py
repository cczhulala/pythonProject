# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 18:03
'''
split()从字符串的左边开始劈分，默认的劈分字符是空格字符串，返回的值都是列表
以参数sep指定劈分的字符
通过maxsplit指定劈分字符串时的最大劈分次数，在经过最大次劈分之后，剩余的子串会单独作为一部分
rsplit()右边开始
'''
s = 'hello world Python'
lst = s.split()
print(lst)

s1 = 'hello|world|python'
print(s1.split(sep='|'))
print(s1.split(sep='|',maxsplit=1))