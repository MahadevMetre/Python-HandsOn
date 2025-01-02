marks = [12, 56, 32, 64, 12, 25, 51]

index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("Awesome!")
    index += 1    


# Enumerate function:
marks = [12, 56, 32, 64, 12, 25, 51]

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Awesome!")