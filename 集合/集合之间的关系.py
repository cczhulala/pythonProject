# 编写人 : 陈昌志
# 开发时间 : 2022/7/28 11:37
'''
判断两个集合是否相等用==和！=
判断一个集合是否是另外一个集合的子集issubset
一个集合是否是另外一个集合的超集issuperset
判断两个集合是否没有交集 isdisjoint
'''

s={10,20,30,40}#集合是无序的
s2={30,40,20,10}
print(s==s2)
print(s!=s2)

s1={10,20,30,40,50,60}
s2={10,20,30,40}
s3={10,20,90}
print(s2.issubset(s1))
print(s3.issubset(s1))
print(s1.issuperset(s2))
print(s2.issuperset(s3))

print(s1.isdisjoint(s2))#是否没有交集，错