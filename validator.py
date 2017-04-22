#BUGS: WHY DO 06002224 AND 06002229 CREATE DIFFERENT OUTPUT?
#FEATURES: IN missing_end_columns, make a new formatted section after the first
# which tests all the inbetween columns as well
# Refactor missing_end_columns to use the check_airwaybill_number function
# When using missing_end_column, in the circumstance the first digit is a zero
# it does not print to the screen
import sys
from termcolor import colored

highlightColour = 'red'

def main():


    userInput = ''

    while userInput != 'quit':
        print("Enter a number between 7 and 8 digits.")
        print('If a column is indecipherable, leave it blank i.e. 12345 78')
        print('If there are only 7 digits shown, it\'s assumed there is a column missing on the end.')
        userInput = str(input('\nEnter your number, \'quit\', or \'help\':'))

        length = len(userInput)

        if userInput == 'help':
            help()
            continue

        try:
            val = int(userInput)
        except ValueError:
            print("Please enter a 7 or 8 digit number only")
            continue

        if length < 7 or length > 8:
            print("\ninvalid Entry.\n")


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
    print("Air waybills consist of a 3 digit airline prefix, a 7 digit serial number and a check digit.")
    print("The prefix can be ignored.  When you divide the serial number by 7, the remainder should match the check digit.")

    print("Note: This program requires Python 3 or above")
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

    # FORMATTING ISSUE: IF FIRST NUMBER IS 0 IT DOES NOT PRINT TO SCREEN
    firstSeven = int(waybill_number)
    remainder = firstSeven % 7
    print(str(firstSeven) + colored(str(remainder), highlightColour))


if __name__ == '__main__':
    sys.exit(main())
