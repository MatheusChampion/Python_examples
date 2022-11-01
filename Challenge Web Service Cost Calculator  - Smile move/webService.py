
from typing import DefaultDict


def main():
    print("----------------------------------------------------------------------------")
    print("                 Welcome to A Web Service Company                           ")
    print("----------------------------------------------------------------------------")
    storage = input("What is your storage needed for hosting your server in GB?  ")

    if (storage.isdigit() == True):
        if(int(storage) == 0):
            print("----------------------------------------------------------------------------")
            print("Are you playing with us? If you want 0, do the math yourself!!!")
            print("----------------------------------------------------------------------------")  
        elif (0 > int(storage) <= 5 ):
            res = int(storage) * 3.99
            print("----------------------------------------------------------------------------")
            print("The " + str(storage) + "GB will cost you, $" + "%.2f" % res + " CAD")
            print("----------------------------------------------------------------------------")
        else:
            res = (((int(storage) - 5) * 5.50) + 19.95)
            print("----------------------------------------------------------------------------")
            print("The " + str(storage) + "GB will cost you, $" + "%.2f" % res + " CAD")
            print("----------------------------------------------------------------------------")
    else:
        print("----------------------------------------------------------------------------")
        print(" ******************** ERROR - Invalid data ******************************** ")
        print("----------------------------------------------------------------------------")
        return


main()