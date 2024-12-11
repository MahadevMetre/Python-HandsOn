# The FizzBuzz logic checks if a number is divisible by 3 (print "Fizz"), 5 (print "Buzz"), or both (print "FizzBuzz").
x = 5

if 3 % x == 0:
    a = "fizz"
    print(a)
else:
    a = ""

if 5 % x == 0:
    b = "buzz"
    print(b)
else:
    b = ""

result = f"{a}{b}"
print(result)
