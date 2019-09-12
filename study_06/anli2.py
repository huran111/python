class Person:
    __age = 18

    def show(self):  # 对象方法
        pass
    @classmethod
    def test(self):
        print(self.__age+20)


p = Person()

p.test()
