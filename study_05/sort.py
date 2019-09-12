numbers=[5,5,6,7,8,4,3,2,2,1]
numbers=sorted(numbers)
print(numbers)
numbers.sort(reverse=True)
print(numbers)
numbers=[5,4,3,2,1]

#自定义排序算法
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i]>numbers[j]:
             numbers[i],numbers[j]=numbers[j],numbers[i]
             print(numbers)
print("==================================================")
myList=[4,1,6,2]
flag=True
for i in range(0,len(myList)-1):
    for j in range(0,len(myList)-i-1):
        if myList[j]>myList[j+1]:
            tmp=myList[j]
            myList[j]=myList[j+1]
            myList[j+1]=tmp
            flag=False
    if(flag):
        break
print(myList)
print("==================================================")
