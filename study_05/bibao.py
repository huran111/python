def func():
    a=100
    def inner_func():
        b=33
        print(a,b)
    return  inner_func
func()()
conatainer = [0]
#閉包的简单应用
def count():

    def add_one():
        conatainer[0]=conatainer[0]+1
        print(conatainer[0])
    return add_one
for i in range(0,3):
    count()()