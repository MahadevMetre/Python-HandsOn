# finally: if anything you wanna stop or break once in for all use this.
def new_func():
    try:
        l = [1, 2, 3, 4, 5]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")    
        return 0
    finally:
        print("I am always executed")
x = new_func()    
print(x)