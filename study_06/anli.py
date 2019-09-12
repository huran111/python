class Dog:
    def __init__(self,nickname):
        self.nickname=nickname
    def run(self):
        print("{}跑来跑去".format(self.nickname))
    @classmethod
    def test(cls):
      print(cls)
      
Dog.test()