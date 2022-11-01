import random

nb=[]

def get_random_numbers():
    numbers = []
    count = 0 
    while count < 6: 
        numbers = random.randint(1,50)
        if numbers not in nb: nb.append(numbers)
        print(nb)
        count += 1

def main():
    print("The random numbers: ", get_random_numbers())

main()