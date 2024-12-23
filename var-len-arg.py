import numbers
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))
average(5, 6,)

#keyword Arbitrary Arguments
def name(**name):
    print("Hello," , name["fname"],
        name["mname"], name["lname"])
name(mname = "Buchanan", lname = "Barnes", fname = "James")

#return
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)
c = average(5, 6,)
print(c)
