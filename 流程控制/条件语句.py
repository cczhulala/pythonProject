# 编写人 : 陈昌志
# 开发时间 : 2022/7/25 22:21
#单分支，多分支，嵌套分支，条件表达式xxx if 条件 else yyyy

age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")    # 1<=a<=5这是正确的
elif age > 2:                   #也可以用else：
    human = 22 + (age - 2) * 5
    print("对应人类年龄: ", human)

### 退出提示
input("点击 enter 键退出")

a = 10;
if a>10 :
    print('a>10')
elif a ==10 :
    print('a=10')
else:
    print('a<10')

#条件表达式
print( ('a==10') if a==10 else ('a!=10'))