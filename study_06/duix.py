class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age
    # def setAge(self,age):
    #     self.__age=age
    # def getAge(self):
    #     return self.__age
    def __str__(self):
        return "姓名{},年龄{}".format(self.name, self.__age)


s = Student("a", 32)
print(dir(Student))
s.age=333
print(s.age)
