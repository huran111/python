import sys


class Person:
    def __init__(self, name):
        self.name = name

    def __del__(self):  # 没有任何引用次数 调用我
        print("delete")

    def __str__(self):
        return self.name+str(id(self))


p = Person("jack")
print(p)
print(dir(Person))