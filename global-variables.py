x = "awesome"

def myfunc():
    z = " man"  # Local variable 'z'
    y = x + z  # Concatenating 'x' (global) and 'z' (local)
    print("Python is " + y)  # Proper indentation for the print statement

myfunc() 