x = 'work on 12-14-2024'
y = 'i will try'

def myfunc():
    global x  # Declaring 'x' as global
    x = y  # Modifying the global variable 'y'

print(x)