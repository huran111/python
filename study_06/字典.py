a = {'name': '胡冉', "age": 13, "gender": "男"}
print(a, type(a))
print(a["name"], a["age"], a["gender"])

d = dict(name="胡冉", age=23, gender="男")
print(d, type(d))
# 也可以将一个包含有一个双值子序列转换为字典
d = dict([("name", "孙悟空"), ("age", 23)])
print(d, type(d))
print(len(d))
# in 是否包含指定的键
print("name" in d)
print("name" not in d)

n = "name"
print(d[n])
# 不存在返回None
print(d.get("name2"))
# 不存在返回默认值
print(d.get("name2", "默认是"))

# 修改字典
d["name"] = "刘德华"
print(d)
d["address"] = "天门山"
print(d)
# 如果已经存在返回旧值，不存在添加
d.setdefault("name", "猪八戒")
print(d)

# update 将其他字典中的值 加入到当前字典中
a={"a":1,"b":2,"c":2}
b={"g":4}
a.update(b)
print(a)
b.update(a)
print(b)
#删除元素
del  a["a"]
print(a)
#随机删除字典中的一个键值对
a.popitem()
print(a)
