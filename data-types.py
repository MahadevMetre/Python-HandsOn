# Automatic type assignment
x = "Hello World"  # str
y = 20             # int
z = 20.5           # float
c = 1j             # complex
fruits = ["apple", "banana", "cherry"]  # list
info = {"name": "John", "age": 36}      # dict
is_active = True    # bool
b = b"Hello"        # bytes
empty = None        # NoneType

print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>
print(type(z))  # Output: <class 'float'>


# Explicitly setting types
x = str("Hello World")       # String
y = int("20")                # Converts a string to int
z = float(20)                # Converts an int to float
c = complex(5, -3)           # Complex number with real and imaginary parts
fruits = list(("apple", "banana", "cherry"))  # Converts a tuple to list
info = dict(name="John", age=36)  # Creates a dictionary
is_active = bool(1)          # Converts 1 to True
b = bytes(5)                 # Creates 5 null bytes
ba = bytearray(5)            # Creates a mutable byte array
fv = memoryview(b)           # Creates a memory view of bytes

print(type(x))  # Output: <class 'str'>
print(type(y))  # Output: <class 'int'>
print(type(z))  # Output: <class 'float'>
print(c)        # Output: (5-3j)
print(type(fruits))  # Output: <class 'list'>


# Converting between data types
x = int("42")  # Convert string to int
y = float(42)  # Convert int to float
z = str(42)    # Convert int to string
fruits = tuple(["apple", "banana", "cherry"])  # Convert list to tuple
nums_set = set((1, 2, 3, 3))  # Convert tuple to set (removes duplicates)

print(x, type(x))  # Output: 42 <class 'int'>
print(y, type(y))  # Output: 42.0 <class 'float'>
print(z, type(z))  # Output: "42" <class 'str'>
print(fruits, type(fruits))  # Output: ('apple', 'banana', 'cherry') <class 'tuple'>
print(nums_set, type(nums_set))  # Output: {1, 2, 3} <class 'set'>


# Using inferred and explicit types
employee = {"name": "Alice", "age": 30, "salary": 55000.75}  # dict
age = int(employee["age"])           # Explicitly converting age to int
formatted_salary = str(employee["salary"])  # Convert salary to string for display

print(f"{employee['name']} is {age} years old and earns ₹{formatted_salary}.")
# Output: Alice is 30 years old and earns ₹55000.75.
