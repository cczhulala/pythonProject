# 编写人 : 陈昌志
# 开发时间 : 2022/7/29 0:17
#返回多个值，返回的是元组,没有返回值可以不写，返回一个的话，是什么就是什么

def fun(num):
    odd=[]#存奇数
    even=[]#存偶数
    for i in num:
        if i%2:
            odd.append(i)
        else:
            even.append(i)
    return odd,even

lst = [10,29,34,23,44,53,55]
print(fun(lst))