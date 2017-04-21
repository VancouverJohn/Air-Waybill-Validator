import sys
from termcolor import colored
highlightColour = 'red'

def main():
    print("Welcome to the Air Waybill Checker.")
    print("This program requires Python 3 or above")
    print("This is meant to help you find the correct number")
    print("of an air waybill when a number is obscured or missing.\n")

    print("Enter a number between 7 and 8 digits.")
    print("If 8 digits, you can leave the indecipherable column blank")
    print("i.e. 123 5678 if the 4th column is indecipherable\n")

    userInput = str(input('Enter your number, or \'quit\':'))

    while userInput != 'quit':

        length = len(userInput)

        if length < 7 or length > 8:
            print("invalid Entry.")
            print("Enter a number between 7 and 8 digits.")
            print("If 8 digits, you can leave the indecipherable column blank")
            print("i.e. 123 5678 if the 4th column is indecipherable\n")

        elif userInput == 'quit':
            break

        else:
            if length == 7:
               missing_end_column(userInput)
               userInput = 'quit'
            else:
                if ' ' in userInput:
                    missing_column(userInput)
                    userInput = 'quit'
                else:
                    if check_valid_airwaybill(userInput) == True:
                        print(colored("Air Waybill Number is Valid", highlightColour))
                        userInput = 'quit'
                    else:
                        calculate_possible_numbers(userInput)
                        userInput = 'quit'

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
        #print(first + colored(str(n), highlightColour) + second)
        for y in range(0, 10):
            # number = int(first + str(y) + second)
            y = str(y)
            print(first + colored(y, highlightColour) + second)
            #if check_valid_airwaybill(str(number)) == True:
            #    print(first + colored(n, highlightColour) + second)

def missing_column(waybill_number):
    first, second = waybill_number.split()
    for n in range(0,10):
        n = str(n)
        testMissingColumn = first + n + second
        if check_valid_airwaybill(testMissingColumn) == True:
            print(first + colored(n, highlightColour) + second)

def missing_end_column(waybill_number):
    firstSeven = int(waybill_number)
    remainder = firstSeven % 7
    print(str(firstSeven) + colored(str(remainder), highlightColour))

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

if __name__ == '__main__':
    sys.exit(main())
