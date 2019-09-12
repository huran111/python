names=["a","b","c","d","e","f"]
print(names[0])
print(names[1])
print(names[-1])
for name in names:
    print(name)



print("----------------------")
names=["a","b","c","d","e","f"]
del  names[0]
print(names)
print("----------------------")
for i in range(len(names)):
    if "a" in names[i] or 'b' in names[i]:
        del  names[i]
print(names)