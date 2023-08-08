class Student:
    native_pace = '吉林'

    def __init__(self,name,age):
        self.name = name  #self.name称为实体属性，进行了一个赋值的操作，将局部的变量name值赋给实体
        self.age = age

  #实例方法，类内叫方法，类外叫函数
    def eat(self):
        print('学生在吃饭')

    @staticmethod
    def method():
        print('静态方法没有self，使用了 staticmethod修饰是静态方法')

    @classmethod
    def cm(cls):
        print('类方法')

def fac():
    print('我绑定了新方法')

#创建Student类的对象
stu = Student('张三',20)
print(id(stu))
print(type(stu))
print(stu)

stu.native_pace = '天津'
print(stu.native_pace)
print(Student.native_pace)

#动态绑定新方法和属性

stu.sale = '男'
print(stu.sale)
stu.fac = fac
stu.fac()