# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 16:07
#向列表的末尾添加元素
lst = [10,20,20]
print('添加元素之前',lst,id(lst))

lst.append(100)
print('添加元素之后',lst,id(lst))#并没有生成新列表，是在原列表基础上添加

#extend（）在列表末尾至少添加一个元素
lst2 = ['hello','world']
lst.append(lst2)#只是将lst2作为一个元素添加到列表中[10, 20, 20, 100, ['hello', 'world']]
print(lst)

lst.extend(lst2)
print(lst)#这是类似一个个添加的效果[10, 90, 20, 20, 100, ['hello', 'world'], 'hello', 'world']


#在任意位置添加元素
lst.insert(1,90)
print(lst)

#在任意位置添加至少一个元素//切片
lst[1:] = lst2
print(lst)#[10, 'hello', 'world'],把1加上1以后的切掉，然后加上新的列表