for i in []:
    print(i)

else:
    print("Sorry no i")    

# Note: if break is used the "else" condition will not be executed
for i in range(5):
    print(i)
    if i == 3:
        break    

#
for x in range(5):
    print("iteration no {} in for loop".format(x+1))  
else:
    print("else block in loop")
    
print("out of loop")  