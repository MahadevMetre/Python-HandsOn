#since 2 has a duplicate value, set will only consider it once
s = {2, 4, 2, 6}
print(s)

#sets doesnt maintain order in the output
info = {"Carla", 22, "Mahadev", 21, "Elon", 50, 19}
print(info)

# Mahadev
mahadev = {}  # this is not a set type, instead its a dictionary
print(type(mahadev))

mahadev = set() # this is a set type
print(type(mahadev))

# access set items
for value in info:
    print(value)

# Methods in sets
# union() and update()
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2)) #union() method
print(s1, s2) #update() method
s1.update(s2)
print(s1, s2)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.intersection_update(cities2)
print(cities)


cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

# isdisjoint() returns True if no items are common
cities = {"Tokyo2", "Madrid2", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

#issuperset() returns True if all items of a set are present in another set
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2))
cities3 = {"Tokyo", "Madrid", "Delhi"}
print(cities.issuperset(cities3))
print(cities3.issuperset(cities))

# add() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)

# remove() method (remove raises a error)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Tokyo")
print(cities)

# discard() method (does not raise an error)
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Tokyo")
print(cities)

# pop() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

# del keyword
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
print(cities)

# clear() method
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities)



