#BUGS: WHY DO 06002224 AND 06002229 CREATE DIFFERENT OUTPUT?
#FEATURES: IN missing_end_columns, make a new formatted section after the first
# which tests all the inbetween columns as well
# Refactor missing_end_columns to use the check_airwaybill_number function
# Change interface to create the ability to enter another query if desired
# (currently the program quits immediately after one query)
# Shrink intro blurb and place in 'help' facility including details 
# of how an air waybill is calculated for validity
# IMPROVE INPUT VALIDATION

import sys
from termcolor import colored

highlightColour = 'red'

def main():

    print('If the 6th column is indecipherable, enter i.e. 12345 78')
    print('If there are only 7 digits shown, enter i.e. 1234567')
    print('Otherwise, enter the full number i.e. 12345678')

    userInput = ''

    while userInput != 'quit':
        userInput = str(input('Enter your number, \'quit\', or \'help\':'))

        if userInput == 'help':
            help()
            continue

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
            else:
                if ' ' in userInput:
                    missing_column(userInput)
                else:
                    if check_valid_airwaybill(userInput) == True:
                        print(colored("Air Waybill Number is Valid", highlightColour))
                    else:
                        calculate_possible_numbers(userInput)

def help():
    print("Welcome to the Air Waybill Checker.")
    print("This program requires Python 3 or above")
    print("This is meant to help you find the correct number")
    print("of an air waybill when a number is obscured or missing.\n")

    print("Enter a number between 7 and 8 digits.")
    print("If 8 digits, you can leave the indecipherable column blank")
    print("i.e. 123 5678 if the 4th column is indecipherable\n")

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


# ADD FUNCTIONALITY TO FIRST CHECK END COLUMNS, THEN WORK WAY THROUGH REST OF COLUMNS
# FORMATTED FOR THE EASE OF THE READERS USE
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
