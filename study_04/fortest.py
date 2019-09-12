print(range(8))
for i in range(8):
    print("hello--->", i)
print("over----------")

for i in range(8):
    if i == 3:
        print("{}吃火锅".format(i))
    print("{}面条".format(i))

num = 1
name = "胡冉"
'''
 pass 标识过
'''
for i in range(num):
    print("{}很饿，正在吃{}个".format(name, i + 1))
else:
    print("还没有馒头{}哭了".format(name))
if 10 > 7:
    print("10是大的")
else:
    pass

while i <= 10:
    print(i)
    i += 1
    n=1
while n<=30:
    if n%3==0:
        print("====",n)
    n+=1
