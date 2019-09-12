A = [1, 2, 3, 4, 5]
print(A)
B = [12, 3, 4];
print(A + B)
a = [2, 3, 4];
print(id(a));
a[0] = '1';
print(a);
print(id(a));
# 元组是不可变的
a = (1, 2, 3);
# 列表是可变的
b = [1, 2, 3];
b.append(4);
print(b);
a = (1, 2, 3, [1, 2, 34]);
print(a[3][0]);
c = 1;
c = c + 1;
print(c);
print(not 1)
print(1 and 0)
print("" and b )
print(" b" and "a")
#判断是属于什么类型的
a="hello"

print(isinstance(a,str))