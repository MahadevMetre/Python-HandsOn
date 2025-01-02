# import ifnameequal.py to main.py
def welcome():
    print("Hey you are welcome my friend")

 # print(__name__)
if __name__ == "__main__":
    welcome()


# main.py    
import ifnameequal.py

ifnameequal.welcome()

