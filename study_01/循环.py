con = True
# while con:
#   print("huran")
a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]
for x in a:
    for y in x:
        print(y)

counter = 1
while counter <= 10:
    counter += 1
    print(counter)
else:  # 当white返回false时候，执行else
    print("EOF")
a=[1,2,3]
for x in a:
    if x==2:
        break
    print(x)
else:
    print("EOF")
print("-------------------------------------------------------------------")