class Student: #Student是类名，可以由一个或者多个单词组成，首字母大写
    pass

student1 = Student()

#一切皆对象，Student也是对象
print(type(student1))
print(id(student1))
print(type(Student))
print(id(Student))