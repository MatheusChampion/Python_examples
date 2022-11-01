
#import methods 
import random
import time

#func to get input
def get_input(count):
    # Receive the count from game()
    number = []
    true = False
    while (true == False):
        guess = input("Enter guess #%-1d between 1 and 100:      " % (count))
        if(guess.isdigit() == True) and ( 0 < int(guess) < 101): 
                # Save the number in the list for verification of repetitive input
                print(number)
                if (guess in number):
                    print(">> YOU'VE ALREADY TRIED IT! HOW ABOUT TRYING A DIFFERENT NUMBER? <<")
                else:
                    number.append(guess)
                    guess = int(guess)
                    return guess
        elif(guess.isdigit() == True):
            print(">>>>>>>>>>>>>>>> MUST BE IN A RANGE FROM 1 TO 100 <<<<<<<<<<<<<<<<<<")
        else:
            print(">>>>>>>>>>>>>>>> INVALID INPUT: PLEASE TRY AGAIN <<<<<<<<<<<<<<<<<<<")

#func to do the verifications
def game():
    # Create a empty list to verify double numbers
    # Create a random number between 1 and 100
    num = random.randint(1, 100)
    # Just for verifications
    print(num)
    count = 0
    # Loop for the 10 tries 
    while(count < 10):
        # Incriase the count for manager the # of tries
        count += 1
        # Get the input from the other function
        guess = get_input(count)
        if(guess == num):
            print("====================================================================")
            print("                     Guess #%d : %d - CORRECT!" % (count, guess))
            print("                       <<<<<    " + str(num) + "   >>>>>>                ")
            print("                       CONGRATS YOU'VE WON                   ")
            print("====================================================================")
            # Wait 2 seconds
            time.sleep(2)
            return 

        elif(guess < num):
            print("Guess #%d : %d - Higher!" % (count, guess))
            print("====================================================================")

        elif(guess > num):
            print("Guess #%d : %d - Lower!" % (count, guess))
            print("====================================================================")
        # Verify repetitive numbers
        # Verify any other number
        # Anything else
    # Lost the game
    print("           ):  YOU HAVE LOST AND THE GAME IS OVER  :(      ")
    print("                >>>>> THE NUMBER WAS %d <<<<<<<<<" % (num))
    print("====================================================================")
    time.sleep(2)
    return

# Main func
def main():
    false = True
    # Loop to play the game forever
    while(false == True):
        print("----------------------- Number Guessing Game -----------------------")
        game()

main()