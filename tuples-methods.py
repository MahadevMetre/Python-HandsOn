#tuples are immutable
#manipulating Tuples
countries = ("Spain", "Italy", "India", "England", "Germany") 
temp = list(countries) 
temp.append("Russia")      #add item
temp.pop(3)                #remove item
temp[2] = "Finland"        #change item
countries = tuple(temp) 
print(countries)  

#concatinate two tuples
countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")  
southEastAsia = countries + countries2
print(southEastAsia)

#since tuples are immutable, we can't change them
#we can only do operations on them
#count
tuple1 = (0, 1, 2, 2, 2, 3, 1, 3, 1, 3, 2)
res = tuple1.count(3)
print('count of 3 in the tuple1 is:', res)

#index
tuple1 = (0, 1, 2, 2, 2, 3, 1, 3, 1, 3, 2)
res = tuple1.index(3)
print('count of 3 in the tuple1 is:', res)

#index in specific portion
tuple1 = (0, 1, 2, 2, 2, 3, 1, 3, 1, 3, 2)
res = tuple1.index(3, 4, 8)
print('count of 3 in the tuple1 is:', res)

#length of tuple
tuple1 = (0, 1, 2, 2, 2, 3, 1, 3, 1, 3, 2)
res = len(tuple1)
print('count of 3 in the tuple1 is:', res)