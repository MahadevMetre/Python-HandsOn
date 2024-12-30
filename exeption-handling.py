a = input("Enter a number: ")
print(f"Multiplication table of {a} is:")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid input!")

print("some lines of code")
print("end of program")
    

# valueError    
try:
  num = int(input("Enter an integer: "))
except ValueError:
  print("Number entered is not an integer.")

except IndexError:
  print("Index Error")  