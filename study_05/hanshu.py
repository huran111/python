def add(a,b):
    pass
add(1,2)

def add(*args):
    print(args)
add(1,2,3,3)
print("=========================")
import  random
def checkcode(n):
    s="sdfsdf232desfdf2dfsf2323"
    code=''
    for i in range(n):
        ran=random.randint(len(s))
        code+=s[ran]
    return  code

