s1 = "sdf msdfl sdf s sd "
result = 's' in s1
print(result)
find = s1.find('s')
print(find)

url = "https://www.bilibili.com/video/av57957614/?p=44"
rfind = url.rfind("/")
print(rfind)
filename = url[rfind + 1:]
print(filename)

# index = "hello".index("x")
# print(index)
s1 = "index lucy lucky aaa"
replace = s1.replace(' ', '#')
print(replace)
msg = "是的发生"
encode = msg.encode("utf-8")
print(encode)
decode = encode.decode("utf-8")
print(decode)

s = "sdfs"
s.isalpha()

# join

new_str = '_'.join('abc')
print(new_str)
list1 = ['a', "b", "c"]
result = "".join(list1)
print(result)
