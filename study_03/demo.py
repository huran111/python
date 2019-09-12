print()
a=1.12386
b=round(a,2)
print(b)

def damage(skill1,skill2):
    damage1=skill1*3
    damage2=skill2*3
    return  damage1,damage2
damages=damage(3,2)
print(damages[0],damages[1])
print(type(damages))

def add(x,y):
    result=x+y
    return result
c=add(y=3,x=2)
print(c)