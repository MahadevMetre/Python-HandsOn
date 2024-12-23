#append
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
l.append(9)
print(l)

#sort
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
l.sort()
print(l)

#desending sort
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
l.sort(reverse=True)
print(l)

#reverse sort
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l)
l.reverse()
print(l)

#index
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(l.index(2))
print(l.index(5))

#count
l = [1, 2, 3, 4, 5, 6, 7, 8, 2]
print(l.count(2))

#copy
l = [1, 2, 3, 4, 5, 6, 7, 8]
m = l.copy()
m[0] = 0
print(l)

#insert
l = [1, 2, 3, 4, 5, 6, 7, 8]
l.insert(1, 899)
print(l)

#extend
l = [1, 2, 3, 4, 5, 6, 7, 8]
m = [900, 1000, 1100]
l.extend(m)
print(l)

#concatinate
l = [1, 2, 3, 4, 5, 6, 7, 8]
m = [900, 1000, 1100]
k = l + m
print(k)
