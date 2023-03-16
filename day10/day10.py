# Functions with outputs
# return is an output keyword eg 0
'''
def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return"You didn't provide a valid inputs."
    formatted_f_name = f_name.title()
    formatted_L_name = l_name.title()
    return(f"{formatted_f_name} {formatted_L_name}")

print(format_name(input("What is your first name? "),input("What is your last name? ")))
'''
# ex 0
'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    if month < 1 or month > 12:
        return("invalid month")
    return month_days[month - 1]




#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
'''
# doc strings """" """ these are used to write  documents about functions
# this what a doc string  look like eg 0
'''
def format_name(f_name, l_name):
    """this will take your first name and last name and format them"""
    if f_name == "" or l_name == "":
        return"You didn't provide a valid inputs."
    formatted_f_name = f_name.title()
    formatted_L_name = l_name.title()
    return(f"{formatted_f_name} {formatted_L_name}")

print(format_name(input("What is your first name? "),input("What is your last name? ")))

'''

# return keeps it for later and print is a one time use

# calculator 
import art


#Add
def add(n1, n2):
    """this will take 2 numbers and add them together"""
    return n1 + n2

#subtract 
def subtract(n1, n2):
    """this will take 2 nnumbers and subtract one from the other"""
    return n1 - n2

#multiply
def multiply(n1, n2):
    """this will take 2 numbers and  multiply one by the other"""
    return n1 * n2

# devide
def devide(n1, n2):
    """this will take 2 numbers and devide one by the other"""
    return n1 / n2


operations = {
"+": add,
"-": subtract,
"*": multiply,
"/": devide}

def calculator():
    print(art.logo)
    num1 = float(input("What is the first number? "))
    for symbol in operations:
        print(symbol)

    should_continue = True

    while should_continue:
        operations_symbol = input("pick an operation  ")

        num2 = float(input("what is the next number? "))

        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)


        print(f"{num1} {operations_symbol} {num2} = {answer} ")

# this will ask if the user wants to continue with the last answer 
        continue_last_result = input(f"if you want to  continue with {answer} type 'y' else   type 'n' if you want to start over: ")

#this will run the loop again with the last answer if the user types "y" else it will quit the loop

        if continue_last_result == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()