# 1. What will be the value of the following Python expression?
# 7, 2, 4, 1
# print(4 + 3 % 5)

#answer = 7
#Explanation: The order of precedence is: %, +. Hence the expression above, on simplification results in 4 + 3 = 7. Hence the result is 7.


# 2.What will be the output of the following Python code?
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
 
#     i + = 1

#answer = error
#Explanation: SyntaxError, there shouldn’t be a space between + and = in +=.

# 3.What are the values of the following Python expressions?

# x = 2**(3**2)
# y = (2**3)**2
# z = 2**3**2
# print(x, y, z)

#answer = 512, 64, 512

#  The following python program can work with ____ parameters.
# def f(x):
#     def f1(*args, **kwargs):
#            print("Sanfoundry")
#            return x(*args, **kwargs)
#     return f1
# Explanation: The code shown above shows a general decorator which can work with any number of arguments.

x=56.236

print("%.2f"%x)