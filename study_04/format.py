name = "胡冉"
print("姓名是:" + name)
age = 18
print("年龄是" + str(age))
print("年龄是:%s" % age)
isMarry = False
print("结婚否？回答:%s" % isMarry)

print("年龄是:%d" % age)

# %f 小数点后面的位数，而且是四舍五入
salary = 2323.2323
print("我的薪水:%.2f" % salary)
'''
    皮卡丘
'''
message = "乔治说：我今年{}岁了,{}幼儿园".format(age, age)
print(message)

# input
usernmae = input("请输入参与游戏者用户名:")
password = input("输入密码:")

print("%s请充值加入游戏" % usernmae)
coins = input("请充值:")
print(type(coins))
print('%s充值成功,游戏币:%s' % (usernmae, coins))

