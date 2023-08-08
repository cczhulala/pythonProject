class Student:
    nativa_pace = '吉林' #直接写在类里的变量称为类属性

    def __init__(self,name,age):
        self.name = name #实体属性，进行了一个赋值操作
        self.age = age
    #实例方法
    def eat(self):
        print('吃饭')

    #静态方法
    @staticmethod
    def method(): #这里面没有self
        print('静态方法')
    #类方法
    @classmethod
    def cm(cls):
        print('类方法')

#类之外定义的是函数，类之内定义的是方法

std = Student("张三",20)
std.eat()         #
Student.eat(std)  #这两行功能相同
std.method()
Student.method()
Student.cm()
std.cm()
print(std.name)
print(std.age)

