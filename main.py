import sys
from termcolor import colored

def main():
    # EXAMPLE OF COLOURED TEXT
    #print(colored('hello', 'red'), colored(' world', 'yellow'))
    userInput = ''
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
            else:
                if check_valid_airwaybill((userInput)):
                    calculate_possible_numbers(userInput)
                    userInput="quit"
                else:
                    print("? Air Waybill Number is valid")
        pass

def check_valid_airwaybill(waybill_number):
    #initial check for validity/ divide 1st 7 numbers by seven check modulus against check digit
    return True
    pass

def calculate_possible_numbers(waybill_number):
    if ' ' in waybill_number:
        first, second = waybill_number.split()
        print(first, second)
    else:
        for x in range(0, 8):
        #print all numbers before x
            print(waybill_number[0:(x)],colored(waybill_number[x], 'green'),waybill_number[(x+1):8], sep ='')
    #print(colored(waybill_number[x], 'green'))
    #print(waybill_number[x:8])
        #print all number after x
    pass

def missing_end_column(waybill_number):

    pass

if __name__ == '__main__':
    sys.exit(main())