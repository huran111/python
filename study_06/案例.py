class Cat:
    type = "猫"

    def __init__(self, nickname, age, color):
        self.nickname = nickname
        self.age = age
        self.color = color

    def eat(self, food):
        print("{}喜欢吃{}".format(self.nickname, food))

    def catch_name(self, color, wight):
        print("{},抓了一直{}kg,{}颜色".format(self.nickname, wight, color))

    def sleep(self, hour):
        if hour < 5:
            pass
        else:
            print("起床。。。")

    def show(self):
        print(self.nickname, self.age, self.color)
cat1=Cat("胡冉",23,"红")
cat1.catch_name("黑色",10)