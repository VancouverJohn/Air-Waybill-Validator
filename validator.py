import sys
from termcolor import colored

highlightColour = 'red'

def main():


    userInput = ''

    while userInput != 'quit':
        print("Enter a number between 7 and 8 digits.")
        print('If a column is indecipherable, leave it blank i.e. 12345 78')
        print('If 7 digits are entered, it\'s assumed there is a column missing on the end.')
        userInput = str(input('\nEnter your number, \'quit\', or \'help\':'))

        length = len(userInput)

        if userInput == 'help':
            help()
            continue

        if all(x.isdigit() or x.isspace() for x in userInput) == False:
            print(colored("\nInput may only contain spaces and numbers\n", highlightColour))
            continue

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
                        print(colored("\nAir Waybill Number is Valid\n", highlightColour))
                    else:
                        calculate_possible_numbers(userInput)

def help():
    print("\nNote: This program requires Python 3 or above\n")
    print(colored("Air waybills consist of a 3 digit airline prefix, a 7 digit serial number, and a check digit.", highlightColour))
    print(colored("This program ignores the prefix.  When you divide the serial number by 7, the remainder should match the check digit.", highlightColour))
    print(colored("This program tests for a valid serial number by dividing it (the serial number) by 7.  The remainder must match the check digit to be a valid air waybill number.", highlightColour))

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
            #print(first + colored(y, highlightColour) + second)
            number = (first + y + second)
            if check_valid_airwaybill(str(number)) == True:
                print(first + colored(y, highlightColour) + second)

def missing_column(waybill_number):
    first, second = waybill_number.split()
    for n in range(0,10):
        n = str(n)
        testMissingColumn = first + n + second
        if check_valid_airwaybill(testMissingColumn) == True:
            print(first + colored(n, highlightColour) + second)


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
                print(colored('0', highlightColour) + waybill_number)
            else:
                print(colored(str(n), highlightColour) + waybill_number)
    firstSeven = int(waybill_number)
    remainder = firstSeven % 7
    firstDigit = int(waybill_number[:1])
    if firstDigit == 0:
        placeHolder = waybill_number[1:]
        print(colored('0', highlightColour) + placeHolder + str(remainder))
    else:
        print(str(firstSeven) + colored(str(remainder), highlightColour))

if __name__ == '__main__':
    sys.exit(main())
