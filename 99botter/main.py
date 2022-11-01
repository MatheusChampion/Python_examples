def count():
    num = 99
    for num in range(99, 0, -1):
        if 3 < num <= 99:
            print(" %i bottles of beer on the wall. %i bottles of beer. Take one down, pass it around, %i bottles of beer on the wall." % (num, num, (int(num) - 1)))
        if num == 3:
            print(" %i bottles of beer on the wall. %i bottles of beer. Take one down, pass it around, %i bottle of beer on the wall." % (num, num, (int(num) - 1)))
        if 0 < num < 3:
            print(" %i bottle of beer on the wall. %i bottle of beer. Take one down, pass it around, %i bottle of beer on the wall." % (num, num, (int(num) - 1)))            

def main():
    count()

main()