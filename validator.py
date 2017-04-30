import sys

highlightStart ='\x1b[5;31;40m'
highlightStop = '\x1b[0m'

def main():

    userInput = ''

    while userInput != 'quit':
        print("\nEnter a number between 7 and 8 digits.")
        print('If a column is indecipherable, leave it blank i.e. 12345 78')
        print('If 7 digits are entered, it\'s assumed there is a column missing on the end.')
        userInput = str(input('\nEnter your number, \'quit\', or \'help\':'))

        length = len(userInput)

        if userInput == 'help':
            help()
            continue

        if all(x.isdigit() or x.isspace() for x in userInput) == False:
            if userInput != 'quit':
                print(highlightStart + "\nInput may only contain spaces and numbers\n" + highlightStop)
                continue
            else:
                break

        if length < 7 or length > 8:
            print("\nInvalid entry.\n")
        elif userInput == 'quit':
            break

        else:
            if length == 7:
               missing_end_column(userInput)
            else:
                if len(userInput.split()) > 1:
                    missing_column(userInput)
                else:
                    if check_valid_airwaybill(userInput) == True:
                        print(highlightStart + "\nAir Waybill Number is Valid" + highlightStop)
                    else:
                        calculate_possible_numbers(userInput)

def help():
    print("\nNote: This program requires Python 3\n")
    print("This program checks a given air waybill number for validity.  It only checks the last 8 digits.")
    print("If an invalid air waybill number is entered, a list of valid potential replacements is displayed.\n")
    print("The first 3 digits of an air waybill make up the " + highlightStart + "airline prefix" + highlightStop + ".  This is not relevant to validity.")
    print("The next 7 digits make up the " + highlightStart + "serial number" + highlightStop + ".")
    print("Dividing the serial number by 7 produces the last (8) digit, called the " + highlightStart + "check digit" + highlightStop + ".")

def check_valid_airwaybill(waybill_number):
    serialNumber = waybill_number[:-1]
    serialNumber = int(serialNumber)
    checkDigit = waybill_number[-1:]
    checkDigit = int(checkDigit)
    remainder = serialNumber % 7
    if remainder == checkDigit:
        return True
    else:
        return False

def calculate_possible_numbers(waybill_number):
    for n in range(0,8):
        first = waybill_number[:n]
        second = waybill_number[n+1:]
        for y in range(0, 10):
            y = str(y)
            number = (first + y + second)
            if check_valid_airwaybill(str(number)) == True:
                print(first + highlightStart + y + highlightStop + second)

def missing_column(waybill_number):
    first, second = waybill_number.split()
    for n in range(0,10):
        n = str(n)
        testMissingColumn = first + n + second
        if check_valid_airwaybill(testMissingColumn) == True:
            print(first + highlightStart + n + highlightStop + second)


def missing_end_column(waybill_number):
    checkDigit = int(waybill_number[-1:])
    middleFive = str(waybill_number[:-1])
    for n in range(0,10):
        n = str(n)
        testFirstSeven = n + middleFive
        testFirstSeven = int(testFirstSeven)
        mod = int(testFirstSeven % 7)
        if mod == checkDigit:
            if n == 0:
                print(highlightStart + '0' + highlightStop + waybill_number)
            else:
                print(highlightStart + str(n) + highlightStop + waybill_number)
    firstSeven = int(waybill_number)
    remainder = firstSeven % 7
    firstDigit = int(waybill_number[:1])
    if firstDigit == 0:
        placeHolder = waybill_number[1:]
        print('0' + placeHolder + highlightStart + str(remainder) + highlightStop)
    else:
        print(str(firstSeven) + highlightStart + str(remainder) + highlightStop)

if __name__ == '__main__':
    sys.exit(main())
