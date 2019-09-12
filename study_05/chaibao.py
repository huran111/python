t1=(4,7,3)
a,b,c=t1
print(a,b,c)

a=t1
print(a)

t1=(2,34,5,6,7,34,55)
a,c,*_=t1
print(a,_,c)

a,*b=t1
print(a,b)  # *b标识未知 0-n
print(*b)
x,y,*z="hello"
print(x,y,z)
print(*[3,4,5])
