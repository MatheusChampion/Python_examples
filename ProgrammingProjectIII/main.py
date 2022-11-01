import csv
from os import close, write
import time
import turtle

wn = turtle.Screen()
wn.title("Make your own story")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

def game(saveLine):
    # Open file
    infile = open("story.csv", "r")
    # Create a CSV Reader object
    csvReader = csv.reader(infile)
    # List to contain data
    storyData = []
    # loop to create a 2D list 
    for row in csvReader:
        storyData.append(row)
    loop = True
    while (loop == True):
        # Chose a random row at the list
        opt = storyData[int(saveLine)]
        while(opt[1] != ""):
            opt1 = opt[3]
            opt2 = opt[4]
            print(opt[0])
            print("1 - " + opt[1])
            print("2 - " + opt[2])
            print("3 - Save Game")
            secondInpt = input(">")
            try:
                secondInpt = int(secondInpt) 
                if (secondInpt == 1):
                    #  '-1' because on the file the list goes 1 - 7, and here it goes 0 - 6, so if on the file the option is '7' it get an error, *** 2h to figure it out :'( ***
                    opt1 = (int(opt1) - 1)
                    opt = storyData[opt1]
                elif (secondInpt == 2):
                    opt2 = (int(opt2) - 1)
                    opt = storyData[opt2]
                elif (secondInpt == 3):
                    # Save the line where we the user are right now
                    saveLine = storyData.index(opt)
                    save(saveLine)
                else:
                    print('\033[91m' + "      Invalid input, please try again   " + '\033[0m')
                    print()
            except:
                print('\033[91m' + "      Invalid input, please try again    " + '\033[0m')
                print()
        print(opt[0])
        time.sleep(2)
        print()
        loop = False    
    infile.close()

def load(saveLine):
    # Verify if the file exist or not
    try:
        file = open("saved.txt", "r")
        saveLine = file.readlines()
        file.close()
        print('\x1b[6;30;42m' + "                  Load Success!                 " + '\x1b[0m')
        return saveLine
    except:
        print('\x1b[6;37;41m' + "         You've no game to load, a new game has started          " + '\x1b[0m')
        saveLine = ['0']    
        return saveLine

def save(saveLine):
    file = open("saved.txt", "w")
    # Save the line in the file
    file.write(str(saveLine))
    file.close()
    print('\x1b[6;30;42m' + "            Save was a Success!          " + '\x1b[0m')
    print()


def main():
    # Colours
    CRED = '\033[91m'
    CEND = '\033[0m'
    saveLine = 0
    while True:
        wn.update()
        # Main Menu
        print("**************  Text Adventure Game v1.0  ***************")
        print("*                                                       *")
        print("*                   Select one option:                  *")
        print("*                                                       *")
        print("*                      1 - New Game                     *")
        print("*                      2 - Load Game                    *")
        print("*                      3 - Quit                         *")
        print("*                                                       *")
        print("*********************************************************")
        firstInpt = input(">")
        # Erro checking
        try: 
            firstInpt = int(firstInpt)
            if(firstInpt == 1):
                game(saveLine)
            elif(firstInpt == 2):
                lineNum = load(saveLine)
                game(lineNum[0][0])
            elif(firstInpt == 3):
                break
            else:
                print(CRED + "        Invalid input, please try again     " + CEND)
                print()
        except:
            print(CRED + "        Invalid input, please try again        " + CEND)
            print()

main()