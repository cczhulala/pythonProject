# Developer: ccz
# Time: 2023/8/9 14:25
class Student:
    native_pace='吉林'#直接写在类里面的变量称为类属性
    def __init__(self,name,age):
        self.name=name#sele.name称为实体属性，进行了赋值操作，将局部变量的值赋值给实体
        self.age=age

    def eat(self):#实例方法，不叫函数，类外定义的才是函数
        print('吃饭')
    #静态方法
    @staticmethod
    def method():#静态方法中不能写self，不能有参数
        print('静态方法')

    @classmethod
    def cm(cls):#类方法传递cls
        print('类方法')