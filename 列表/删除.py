# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 16:17
"""
remove  一次删除一个元素，重复元素删除第一个，不存在报错
 pop    删除一个索引上的元素，索引不存在报错，不指定的话删除最后一个元素
  切片
   clear  清空列表
    del   删除列表
    """
lst = [10,20,30,40,50,60]
lst.remove(30)
print(lst)

lst.pop(0)
print(lst)
lst.pop()
print(lst)

#切片，会产生新的列表对象
lst2 = lst[1:3]
print(lst,id(lst))
print(lst2,id(lst2))

#不产生新的列表对象,使用空列表替换
lst[1:3]=[]
print(lst)

lst.clear()
print(lst)

del lst
print(lst)#会报错