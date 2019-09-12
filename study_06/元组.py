# 元组 tuple 元组是一个不可变的序列
# 创建了一个空元组
my_tuple = ()
print(my_tuple, type(my_tuple))
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[3])

my_tuple = 2, 3, 4, 5, 6
print(type(my_tuple))
# 解包
a, b, c, d, e = my_tuple
print("a=", a)
print("d=", b)
print("c=", c)
print("d=", d)
print("e=", e)
# 交互
a = 100
b = 300
# 解包  实现变量交换
print(a, b)
a, b = b, a
print(a, b)

# *c是一个列表
a, b, *c = my_tuple
print(a)
print(b)
print(c)

a, *b, c = my_tuple
print(a)
print(b)
print(c)

