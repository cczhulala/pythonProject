# Developer: ccz
# Time: 2023/8/9 14:25
class Student:
    native_pace='吉林'#直接写在类里面的变量称为类属性
    def __init__(self,name,age):
        self.name=name#sele.name称为实体属性，进行了赋值操作，将局部变量的值赋值给实体
        self.__age=age

    def eat(self):#实例方法，不叫函数，类外定义的才是函数
        print('吃饭')
    #静态方法
    @staticmethod
    def method():#静态方法中不能写self，不能有参数
        print('静态方法')

    @classmethod
    def cm(cls):#类方法传递cls
        print('类方法')

stu=Student('张三',18)
print(id(stu))
print(type(id))
print(stu)
stu.eat() #对象名.方法名()
print(stu.name)
#访问被封装的属性
print(stu._Student__age)

Student.eat(stu)#28行与24行相同   类名.方法名(类的对象)-->实际上就是方法处定义的self
#类属性是所有对象共享的
print(stu.native_pace)
print(type(stu.native_pace))
#可修改
Student.native_pace='121'
print(stu.native_pace)
#如果使用创建的stu.native_pace = '福建'，
# 那么只是让stu中的变成福建，类中并没有变化

stu.native_pace='474'
print(stu.native_pace)
#类方法使用方式
Student.cm()
stu.cm()
#静态方法
Student.method()
stu.method()

stu1=Student('李四',20)

stu.money=18
print(stu.money)
#print(stu1.money)是错误的
#给类动态绑定属性
Student.s=88
print(stu.s)
#动态绑定类方法
def fun(a):
    print(a)

stu.f=fun
print(stu.f(777))
print(type(stu.f))