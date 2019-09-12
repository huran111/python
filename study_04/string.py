s1 = "abc"
s2 = "abc"
s3 = '''abc'''  # 三引号占用的内存空间与单引号的不同
print(id(s1), id(s2), id(s3))
print(s1 == s2)
print(s1 is s2)

print(s2)
print(s3)

# s1=input("请输入:")
# s2=input("请输入:")
print(s1 == s2)
print(s1 is s2)

name = "steven"
result = 'eve' not in name
print(result)

print("%s说:%s" % (name, "好好学习"))
print(r"%s说:\'哈哈哈\'" % (name))
fileName = 'huran.png'
print(fileName[1])
print(fileName[0:7])
print(fileName[1:])
print(fileName[-1])
print(fileName[::-1])
str1 = "1234567"
print(str1[-5:-1])  # -1 倒序 1 正序（可不加）
print(str1[5:0:1])
