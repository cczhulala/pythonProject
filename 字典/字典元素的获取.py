# 编写人 : 陈昌志
# 开发时间 : 2022/7/27 17:21

#s['李四'] 不存在报错
#s.get('李四')  不存在返回None，可以设置返回别的

score = {'张三':100,'李四':200}
print(score['张三'])
print(score.get('张三'))
print(score.get('99',99))#key不存在时提供的默认值

