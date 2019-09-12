a = 1;
b = 2;
c = 4;
print(not a or b + 2 == c)
'''
条件控制语句，循环控制  ，分支
'''
mood = False
if mood:
    print("go to left")
    print("go tototo left")
else:
    print("go tototo left")
print("go tototo111 left")

account = '123'
password = '123'
print('please input account')
user_account = input()
print('please input password')
user_password = input()
if (account == user_account and password == user_password):
    print(user_account)
    print(user_password)
else:
    print("账号或者密码不相等")
# ------------------------------------------------------------
a = True
if a:
    print("a")
else:
    print("b")
for target_list in exp:
    pass


class classname(object):
    pass


@staticmethod
def funcname(paramter_list):
    pass
