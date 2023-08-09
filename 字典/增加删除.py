# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 17:26
score = {'张三':100,'李四':200}
#判断是否在里面
print('张三' in score)
print('xx' not in score)

#删除
del score['张三']#删除键值对
print(score)

score.clear()#清空
print(score)
#增加
score['陈六'] = 100
print(score)

#修改
score['陈六'] = 200
print(score)