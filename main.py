import sys

def main():

    print("Welcome to the Air Waybill Checker.")
    print("This is meant to help you find the correct number")
    print("when a number is obscured or missing.\n")

    print("Enter a number between 7 and 8 digits.")
    print("If 8 digits, enter the column number that is indecipherable (1-8)")

    #userInput = str(sys.argv[1])
    userInput = str(input('Enter your number:'))

    if len(userInput) < 7 or len(userInput) > 8:
        print('Please Enter Between 7 or 8 Digits.')

    else:
        waybillNumber = int(userInput)
        print(waybillNumber + 2)

    pass

def calculate_possible_numbers(waybill_number, questionable_column):

    pass

def missing_end_column(waybill_number):

    pass

if __name__ == '__main__':
    sys.exit(main())