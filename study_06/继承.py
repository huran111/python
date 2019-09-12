import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        ran_time = random.randint(1, 10)
        msg = "{}品牌{}以{}速度行驶{}小时".format(self.brand, road.name, self.speed, ran_time)
        print(msg)

    def __str__(self):
        return "{}品牌的,速度：{}".format(self.brand, self.speed)


r = Road("兰交高速", 121)
car = Car("奥迪", 123)
car.get_time(r)