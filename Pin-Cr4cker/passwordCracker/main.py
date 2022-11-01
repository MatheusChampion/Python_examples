import itertools
from itertools import combinations
import time
import random

def generatePassword(glyphs):
    # generate the password to crack (3 glyphs long)
    passwordToCrack = ""
    for n in range(3):
        # add a glyph to the password
        passwordToCrack = passwordToCrack + glyphs[random.randint(0, len(glyphs))]

    print("PASSWORD TO CRACK:", passwordToCrack)
    time.sleep(2)
    return passwordToCrack

def main():
    # list of possible glyphs that make up the password
    glyphs = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9"]
    
    passwordToCrack = generatePassword(glyphs)

    # write the code to crack the password here!
    # ...
    guess = ""
    count = 0
    while (guess != passwordToCrack):
        for x in range(passwordToCrack):
            count += 1
            print("Crack Attempt #%d: %s" % (count, x))
            for y in range(passwordToCrack):
                print("Crack Attempt #%d: %s%s " % (count, x, y, ))
                for z in range(passwordToCrack):
                    print("Crack Attempt #%d: %s%s%s " % (count, x, y ,z))
                    if (x != y) & (y != z) & (z !=x ):
                        print("Password Cracked (%s%s%s)!" % (x,y,z))
                        break
        # for letter in combinations(glyphs ,len(passwordToCrack)):
        #     count += 1
        #     guess = ''.join(letter)
        #     print("Crack Attempt #%d: %s " % (count, guess))
        #     if guess == passwordToCrack:
        #         print("Password Cracked (%s)!" % (guess))
        #         break
main()