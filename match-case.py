x = int(input("Enter a number: "))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("x is four")
    case _:
        print(x)