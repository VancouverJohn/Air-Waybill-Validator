import sys
from termcolor import colored

def main():
    # EXAMPLE OF COLOURED TEXT
    #print(colored('hello', 'red'), colored(' world', 'yellow'))
    userInput = ''
    print("Welcome to the Air Waybill Checker.")
    print(colored('This program requires Python 3 or above', 'green'))
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
               print("we have 7")
            #print(len(userInput.split()))
            else:
                #print((userInput.split()))
                calculate_possible_numbers(userInput)
                userInput="quit"
        pass

def calculate_possible_numbers(waybill_number):
    for x in range(0, 8):
        #print all numbers before x
        for y in range (0, x):
            print(waybill_number[y])
        print(colored(waybill_number[x], 'green'))
        for z in range (x, 8):
            print(waybill_number[z])
        #print all number after x
    pass

def missing_end_column(waybill_number):

    pass

if __name__ == '__main__':
    sys.exit(main())