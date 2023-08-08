# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 22:48
'''
replace() 第一个参数指定背替换的子串，第二个参数指定替换子串的字符串，
返回替换后得到的字符串，替换前的字符串不发生变化，调用该方法时可以通过第三个参数指定最大替换次数
join()字符串合并，将列表或元组中的字符串合并成一个字符串
'''
s = 'hello,world'
print(s.replace('world','python'))
s = 'hello,world,world,world,world'
print(s.replace('world','python',2))


s1=['python','world','java']
print('|'.join(s1))

t = ('hello','java',"python")
print(''.join(t))

print('*'.join('python'))#把python当成字符串序列进行连接