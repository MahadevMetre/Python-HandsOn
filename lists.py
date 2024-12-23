marks = [3, 5, 6, 7, 8, 9, 10, 11]
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

print(marks)
print(marks[:])
print(marks[1:7])
print(marks[1:7:2]) #jump index


#printing alternate values
animals = ["cat", "dog", "bat", "mouse", "pig", "horse","donkey", "goat", "cow"]
print(animals[::2]) #using positive indexes
print(animals[-8:-1:2]) #using negative indexes