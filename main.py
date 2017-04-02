import sys

def main():

    userInput = ''
    print("Welcome to the Air Waybill Checker.")
    print("This is meant to help you find the correct number")
    print("when a number is obscured or missing.\n")

    print("Enter a number between 7 and 8 digits.")
    print("If 8 digits, enter the column number that is indecipherable (1-8)")

    userInput = str(input('Enter your number, or \'quit\':'))

    while userInput != 'quit':

        if len(userInput) < 7 or len(userInput) > 8:
            print('\nPlease Enter Between 7 or 8 Digits.')

        elif userInput == 'quit':
            break
        else:
            waybillNumber = int(userInput)
            print(waybillNumber + 2)

        print("If 8 digits, enter the column number that is indecipherable (1-8)")

        userInput = str(input('Enter your number, or \'quit\':'))

        pass

def calculate_possible_numbers(waybill_number, questionable_column):

    pass

def missing_end_column(waybill_number):

    pass

if __name__ == '__main__':
    sys.exit(main())