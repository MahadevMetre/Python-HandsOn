# generating list on the fly
lst = [i for i in range(4)]
print(lst)

#scene2
lst = [i*i for i in range(4)]
print(lst)

#condition
lst = [i*i for i in range(10) if i%2==0]
print(lst)
