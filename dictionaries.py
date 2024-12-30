dic = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

print(dic["name"])


dic = {
    344: "Mahadev",
    342: "Raj",
    345: "Rajesh"
} 

print(dic[344])

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info['name'])
print(info.get('name'))

# all keys info
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
print(info)
print(info.keys())
print(info.values())

# also

for key in info.keys():
    print(f"The value corresponding to the key {key} is {info[key]}")


ep1 = {122:45, 123:89, 567:69, 670:69}
ep2 = {222: 67, 566: 90}  
ep1.update(ep2)
print(ep1)

# also particular
ep1.pop(122)

# pop end keyword
ep1.popitem()
del ep1[122]
print(ep1)

