#recursions are basically functions.
#recursions call the function in the same function.

#factorial(7) = 7*6*5*4*3*2*1
#factorial(7) = 7*factorial(6)
#factorial(6) = 6*factorial(5)
#factorial(5) = 5*factorial(4)
#factorial(4) = 4*factorial(3)
#factorial(3) = 3*factorial(2)
#factorial(2) = 2*factorial(1)
#factorial(1) = 1

def factorial(n):
    if (n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
print(factorial(4))
print(factorial(5))

#Brief
# first goes to else is True, since if has "if (n==0 or n==1):" 
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1), now if has "if n==1, 
# 5 * 4 * 3 * 2 * 1
# 120

#
f = 5
n = 3
f(0) = 0
f(1) = 1
f(2) = f(1) + f(0)
f(n) = f(n-1) + f(n-2)    

#QUICK QUIZ: Write a program to print the fibonacci sequence
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)