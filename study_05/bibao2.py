def func(number):
    a = 100

    def inner_func():
        nonlocal  a
        nonlocal  number
        number += 1
        for i in range(number):
            a += 1
        print("修改后a的值:", a)

    return inner_func


func(4)()
#########
a = 50
func(a)()


def test():
    print("=====2222=====")


t = test
t()


# 定义一个装饰器
def decrator(func):
    a = 100

    def wrappper():
        print("--------111")
        func()
        print("--------222")

    return wrappper

#定义装饰器
@decrator
def house():
    print("毛坯房")

house()