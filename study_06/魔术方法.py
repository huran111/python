class Person:
    def __init__(self):
        print("init")
    def __new__(cls, *args, **kwargs): #
       return object.__new__(cls)
p=Person()