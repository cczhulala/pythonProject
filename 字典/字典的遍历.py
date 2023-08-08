# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 23:19
#实际上获取的字典中的键
score = {'a':100,'b':200}
for item in score:
    print(item,score[item],score.get(item))#根据键获取元素的值