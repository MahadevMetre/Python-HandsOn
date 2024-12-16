#endswith()
str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 4, 10))

#find
str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))

#index
# str1 = "He's name is Dan. He is an honest man."
# print(str1.index("ishh"))

#isalnum
str1 = "Welcome00"
print(str1.isalnum())

#isalpha
str1 = "Welcome00"
print(str1.isalpha())

#islower
str1 = "hello world"
print(str1.islower())

#isprintable
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())

#isspace
str1 = "        "
print(str1.isspace())

#istitle
str1 = "World Health Organization"
print(str1.istitle())

#isupper
str1 = "WORLD HEALTH ORGANIZATION"
print(str1.isupper())

#startswith
str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

#swapcase
str1 = "He's name is Dan. Dan is an honest man."
print(str1.swapcase())