import math

def getInput():
    try:
        return int(input("Enter change to return to customer: "))
    except ValueError:
        print("Erro - incorrect input ;(")
        return 0

def calcOutput(change):
    print("$" + str(change), " of change to return to the customer:")

    twenties = math.floor(change / 20)
    change = change - (twenties * 20)
    
    fives = math.floor(change / 5)
    change = change - (fives * 5)
    
    ones = change

    print("Number od $20s =", twenties)
    print("Number od $5s =", fives)
    print("Number od $1s =", ones)

def main():
    change = getInput()

    calcOutput(change)
main()