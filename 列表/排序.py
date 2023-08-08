# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 16:32
#sort()默认从小到大，可以用reverse = True进行降序
#sorted降序

lst = [10,50,30,40]
lst.sort()
print(lst)#排序是在原列表上进行

lst.sort(reverse=True)
print(lst)

new_lst = sorted(lst)#会产生新的列表
print(new_lst)

new_lst = sorted(lst,reverse=True)#会产生新的列表
print(new_lst)