s = lambda a, b: a + b

print(s(1, 2))
list1 = [3, 4, 5, 6]
print(max(list1))
dict1 = {"a": "1", "b": "2"}
list2 = [{"a": "1", "b": "2"}, {"a": "11", "b": "22"}]

print(max(list2, key=lambda x: x["a"]))

list3 = [1, 2, 3, 4, 5, 6, 7]
result = map(lambda x: x + 2, list3)
print(list(result))
result = map(lambda x: x if x % 2 == 0else x + 1, list3)
print(list(result))

# for index,i in enumerate(list3):
#     if i%2!=0:
#         list3[index]=i+1
from functools import reduce
tuple1=(1,2,3,4,5,6,7)
result=reduce(lambda x,y:x+y,tuple1)
print(result)
result=filter(lambda  x:x>4,tuple1)
print(list(result))
