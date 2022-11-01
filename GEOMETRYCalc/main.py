import math
import datetime as dt

def getInput():
    radius = float(input("Enter the radius of the circle: "))
    precision = input("Enter the decimal precision: ")
    return radius, precision

def showCalc(circumference, area, precision):
    # print("Circunference: ", circumference)
    # print("Area : ", area)

    # % = module operator, get the remain 

    print(("%15s %-10" + precision + "f") % ("Circunference: ", circumference))
    print(("%15s %-10" + precision + "f") % ("Area: ", area))
    # print("Area : %15s %-10.3f" % (area))


    print("Calculations made on ", dt.datetime.today())

def main():
    radius, precision  = getInput()
    print(radius)

    circumference = 2 * math.pi * radius
    area = math.pi * math.pow(radius, 2) 

    showCalc(circumference, area, precision)

main()