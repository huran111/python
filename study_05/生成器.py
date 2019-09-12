newList = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(newList)

def gen():
    i=0
    while i<5:
        temp=yield  i #yield 生成器
        print("temp:",temp)
        i+=1
    return "没有更多的数据"
g=gen()
print(g.send(None))
# print(next(g))
# print(next(g))
# print(next(g))
g.send("hello")

def func():
    n=0
    while True:
        n+=1
        yield  n # return n 暂停

print(func().__next__())
