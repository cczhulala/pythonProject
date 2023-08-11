# Developer: ccz
# Time: 2023/8/11 15:51
import math
lst=[]
for num in range(100,1000):
    ge=num%10
    shi=math.floor(num/10)%10
    bai=math.floor(num/100)
    if math.pow(ge,3)+math.pow(shi,3)+math.pow(bai,3)==num:
        lst.append(num)
print(lst)
#这里会输出0而不是000，千年虫问题
print(str(000))


#sasdas