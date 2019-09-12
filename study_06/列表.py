a = [1, 2, 3]
print(a, id(a))
a[0] = 10
print(a)

print(a, id(a))
b=a
b[0]=10
print(a)

# ==  != is   is  not

#== ,!=比较的值， is  , is not 比较的是id

a=[1,2,3]
b=[1,2,3]
print(id(a),id(b))
print(a==b)
print( a is b)