class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        print(self.name,self.age)

class Student(Person):
    def __init__(self,name,age,sale):
        super().__init__(name,age)
        self.sale = sale
    def info(self):
        super().info()
        print(self.sale)

class Teacher(Person):
    def __init__(self,name,age,year):
        super().__init__(name,age)
        self.year = year

stu = Student('张三',20,'男')
stu.info()