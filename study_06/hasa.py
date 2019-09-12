class Computer:
    def __init__(self,brand,type):
        self.brand=brand
        self.type=type
    def online(self):
        print("上网")
class Book:
    pass
class Student:
   def __init__(self,name,computer,book):
       self.name=name
       self.computer=computer
       self.books=[]
       self.books.append(book)

