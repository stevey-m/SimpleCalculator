import math # import the maths module to complete the square root

# we define our function, calculate which has no parameters/arguments set, and present a list to make a selection
def calculate():
    operation = input('''
Please select the number of the operation you would like to complete:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponent(power)
6. Square Root
''')
    operation_funt(operation)
# Try to add fractions

# BELOW
# Taking 2 inputs on a single line with a comma to separate them for 1 to 5
# Square root prompts for 1 input and is using a float
# Can this be optimized

def operation_funt(operation):
    if operation == '1':
        number_1, number_2 = [int(x) for x in input("Enter two values using the following format x,y\n").split(',')]
        print('The value of {} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

# here we write a code for other operations
# we also add if and else if (elif) statements

    elif operation == '2':
        number_1, number_2 = [int(x) for x in input("Enter two values using the following format x,y\n").split(',')]
        print('The value of {} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operation == '3':
        number_1, number_2 = [int(x) for x in input("Enter two values using the following format x,y\n").split(',')]
        print('The value of {} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operation == '4':
        number_1, number_2 = [int(x) for x in input("Enter two values using the following format x,y\n").split(',')]
        print('The value of {} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    elif operation == '5':
        number_1, number_2 = [int(x) for x in input("Enter two values using the following format x,y\n").split(',')]
        print('{} raised to the power of {} = '.format(number_1, number_2))
        print(number_1 ** number_2)

    elif operation == '6':
        number_1 = float(input("Enter a value\n"))
        print('The square root of {} = '.format(number_1))
#        num_sqrt = number_1 ** 0.5
#       print(num_sqrt)
        print(math.sqrt(number_1))

    else:
        print('You have not typed a valid operator, please run the program again.')

    # Add again() function to calculate() function
    again()

# we add the again function to the calculate as a loop
# to make the calculator continuous we define another variable for continuity called again
def again():
# we will need to take input form user
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')
# if the usr selects Y, then call calculate
# we can make the program accept Y or y by adding the .upper()
    if calc_again.upper() == 'Y':
        calculate()
# if the user types N, say thanks and goodbye
# we can make the program accept N or n by adding the .upper()
    elif calc_again.upper() == 'N':
        print('See you later.')
# if the user types any other key aside N, call again until Y or N is entered
    else:
        again()

# Call calculate() outside of the function
# The main function which starts the game
if __name__ == "__main__":
    calculate()
    print()
