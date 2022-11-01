def getInput():
    print("------------------------------------------")
    value = input("Enter the price of the item: ")
    print("------------------------------------------")
    return float(value)

def calc(value):
    tax = (value * 0.15)
    total = (value + tax)
    print("Subtotal  $%.2f" % (value))
    print("Sales Tax $%.2f" % (tax))
    print("------------------------------------------")
    print("Total     $%.2f" % (total))
    print("------------------------------------------")

def main():
    value = getInput()
    calc(value)

main()