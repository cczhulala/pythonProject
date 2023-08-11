# Developer: ccz
# Time: 2023/8/11 14:54
#向文件输出‘奋斗成就更好的你’
#方法一，使用print
fp=open('D:\program_learing\pythonProject\实操案例1\demo1.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()

#方法二，使用文件读写操作
with open('D:\program_learing\pythonProject\实操案例1\demo1.txt','w') as afile:
    afile.write('奋斗成就更好的你')
