t1 = ()
print(type(t1))
t2 = (1)
print(type(t2))
t2 = ("hello")
print(type(t2))
t3 = ("aa", "bb")
print(type(t3))
import random

list = []
for i in range(10):
    ran = random.randint(1, 20)
    list.append(ran)
print(list)
t5 = tuple(list)  # 列表转元组
print(t5)
print(t5[-1])
print(t5[::-1])
print(max(t5))
print(min(t5))
print(sum(t5))
print(len(t5))
print("=============================================")
print(t5.count(6))
print(t5.index(4))
