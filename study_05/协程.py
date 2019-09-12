def task1(n):
    for i in range(n):
        print("搬砖{}".format(i))
        yield None


def task2(n):
    for i in range(n):
        print("听歌{}".format(i))
        yield None


g1 = task1(4)
g2 = task2(5)
while True:
    try:
        g1.__next__()
        g2.__next__()
    except:
        pass
