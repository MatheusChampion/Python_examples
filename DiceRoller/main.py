import random

def NUMBER():
    numb = random.randint(1, 9)
    return numb

def main():
    print("This week's winning lottery number is: ")
    print(str(NUMBER()) + str(NUMBER()) + str(NUMBER()) + str(NUMBER()))

main()