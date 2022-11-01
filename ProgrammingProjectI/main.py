import random


def get_input():
    #Give the variable a valdation as 'false' to beggining the loop
    validated = False
    #While the valited keeps returning 'false' it will keep the code in the loop
    while(validated == False):
        #Demand input to validation of variable
        insult = input("How many insults would you like? ")
        #Verify if the input is a digit and is greater than 0. 
        if ((insult.isdigit() == True) and (int(insult) > 0)):
            #If pass my condition it will enter in the next condition to verify the next question
            #get the input to verify the next condition
            name = input("What is the name of the victim? ")
            #Verify if the name is a string, than start the next condition
            if (name.isalpha() == True):
                #Get the input to verify the next condition
                adj = input("What is the number of adjectives to include in? ")
                if ((adj.isdigit() == True) and (0 <= int(adj) <= 3)):
                    #return the values to the main function, as the command 'return' end the function, there is no need to change the value of the 'validator' and end the loop!
                    return insult, name, adj
                else:
                    #Print the erro according to the condition where it was input wrong and return to beggin the loop again
                    print("====================================================================")
                    print("       Error - You must enter 1, 2 or 3 !! Please try again")
                    print("====================================================================")
            else:
                #Print the erro according to the condition where it was input wrong and return to beggin the loop again
                print("====================================================================")
                print("        Error - It must be a STRING !! Please try again")
                print("====================================================================")
        else:
            #Print the erro according to the condition where it was input wrong and return to beggin the loop again
            print("====================================================================")
            print("       Error - You must enter a NUMBER > 0!! Please try again")
            print("====================================================================")
            
def generate_adj(name, adj):
    #Create lists
    of_adj = ['fat', 'fancy', 'repulsive', 'magnificent', 'colossal', 'large', 'silly', 'skinny', 'lazy', 'massive']
    of_noun = ['jackass', 'dork', 'dingbat', 'jerk', 'stupid', 'dingbat']
    #Condition 1
    if(int(adj) == 1):
        print(name + " is a " + random.choice(of_adj) + " " + random.choice(of_noun) + "!")
    #Condition 2
    elif (int(adj) == 2):
        #Create count to the loop
        count = 0
        #start the quote
        print(name + " is a", end="")
        # Loop to count adjetives
        while ( count < 2):
            #place the asjetives 
            print(" " + random.choice(of_adj), end="")
            count += 1
        # Print the noun 
        print(" " + random.choice(of_noun) + "!")
    # Same thing but with one more loop
    else:
        count = 0
        print(name + " is a", end="")
        while (count < 3):
            print(" " + random.choice(of_adj), end="")
            count += 1
        print(" " + random.choice(of_noun) + "!")

def main():
    ans = "y"
    while (ans == "y"):
        #attribute the values according to the return from the function 'get_input'
        insult, name, adj = get_input()
        count = 0
        while (count < int(insult)):
            #Getting the function generate_adj and sending the data from get_input to be used
            generate_adj(name, adj)
            count += 1
        #Get input to see if the user want to run again!
        ans = input("Want to insult more? (Y or N) \n").lower()
    else:
        print("The aplication was terminated, Thank you!")

main()
