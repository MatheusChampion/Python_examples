

def main():
    ans = input("Would you like to make the smile move? [y/n]  ")
    print(":)")

    #verify if the player want to play
    try:
        ans.lower == 'y'
        #loop to make the game play until the person does want anymore
        while (ans.lower() == 'y'):
            space = input("How many characters would you like to move :)?  ")
            #verify if the input is valid
            if (space.isdigit() == True ):
                if (0 < int(space) <= 40):
                    sml = ":)"
                    #Get the sml and add the Right justified(add to the left) # in int from the input 'space'in whole number and what to sub in for 'space' # in the next argument
                    print(sml.rjust(int(space), ' '))
                    ans = input("Would you like to make the smile move again? [y/n]  ")
                else:
                    print("x( [Your input killed :)]")
                    break
            else:
                print("x( [Your input killed :)]")
                break
        else:
            print("You cannot make the smile move anymore :(")
    except:
         print("You cannot make the smile move anymore :(")
main()