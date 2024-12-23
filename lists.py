marks = [3, 5, 6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

#negative indexing
print(marks[-3])

#convert negative indexing to positive indexing
print(marks[len(marks)-3])
print(marks[3-3])
print(marks[0])

if 7 in marks:
    print("Yes")
else:
    print("No")