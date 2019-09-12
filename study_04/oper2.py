a = 9
b = 2
result = a * b
print(result)

result2 = a ** 4  # 8*8
print(result2)

result = a // b  # // 整除
print(result)
id(a)

# age=20
# age1=20
# print(age is age1)
# print(id(age),id(age1))

age = 23232314
age1 = 23232314
print(age is age1)
print(id(age), id(age1))

# 二进制
a = 30
print(bin(a))  # 0b11

b = 0b11110
print(int(b))

c = -8
print(bin(c))
# 位运算 0o开头是八进制
d = 0x9  # 0x 16进制  0-9 a-f
print(int(d))
d = 0xab18
print(d)
'''
1 true 0 false     and 
 0000 0011
 0000 0010
------------
 0000 0010
结果为2
'''
print(3 & 2)

'''
    1 true 0 false    or 
    0000 0101
    0000 0011
    ---------
    0000 0111
'''
print(5 | 3)

'''
 0000 0101
 1111 1010
 ---------
 看第一位符号位 1就是负数0就是整数
  
 减一操作
 1111 1010  -1
 1111 1001
 取反
 0000 0110
 

'''
print(~5)

# ^ 异或 相同0 不同1
print(3 ^ 5)
'''
 0000 0011
 0000 0101
 ---------
 0000 0110
 
'''
# 左移
print(2 << 1)
'''
0000 0010
0000 0100
'''
print(2 >> 1)

# 三木运算符
a=6
b=5
result=(a+b) if a>b else (b-a)
print(result)
username=''
if username=='':
    print("登录")
else:
    print("--------------")