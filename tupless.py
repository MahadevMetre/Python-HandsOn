tup = (1, 2)
print(type(tup), tup)

#scene2
tup = (1)
print(type(tup), tup)

#scene3
#python gets confused when given a single integer the type changes to "int" so solution below:
tup = (1,)
print(type(tup), tup)

#tuple example1
tuple1 = (1, 2, 3,4, 5, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

# NOTE: positive indexing and negative indexing is same as list

#tuple example2
tup1 = (1, 2, 76, 342, 32, "green", True)

if 342 in tup1:
    print("Yes 342 is present in this tuple")

#slicing
tup2 = tup1[1:4]
print(tup2)
