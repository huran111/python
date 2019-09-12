number = 100


def func():
    global number
    number += 1


def chu(a, b):
    return a / b


names = ['tom', 'huran', 'sdf', "sdfsd", "sd", "ddd", "dfsdf"]
result = [name for name in names if len(name) > 3]
print(result)
newList = [i for i in range(1, 100) if i % 3 == 0 and i % 5 == 0]
print(newList)
newList=[(x, y) for x in range(5) if x %2==0 for y in range(10) if y % 2 != 0]
print(newList)


list1=[[1,2,3],[4,5,6],[7,8,9]]
newList=[i[-1] for i in list1]
print(newList)
#集合推导式
dicts={"a":"A","b":"B","c":"C","d":"D"}
newList={value:key for key ,value in dicts.items()}
print(newList)
result=[x*3 for x in range(10)]
print(result)
#得到生成器
result=(x*3 for x in range(10))
print(result)
print(result.__next__())
print(next(result))
print(next(result))
print(next(result))

