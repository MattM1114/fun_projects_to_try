# data types strings, int, float, booleans , lists , dict, sets 

#string eg "Hello" they are a string of characters incased in quotation marks ' ', " ",''' ''', or """ """ 
# the triple ones are for long strings that are on multiple line

# this is called subscripting remember the first character is 0 , we use this dissect strings 

'''
print("Hello"[0])
'''

# integer are whole numbers eg 1 
'''
print(123 + 345)
'''

# when writing large number use _ instead of , eg 123_456_789

#float or floating point number is a number with a decimal place eg 1.2

#bool or boolean is true or False 

# type() is a function that tells you the data type 

# this is how to change to change a int in to a str and how to change a str into int

# eg 0
'''
num = 123
str(num)
'''
'''
num = "123"
int(num)
'''

# this is an eg of conversion 
'''
print(70 + float('100.5'))
'''


# ex 0 
'''
two_digit_num = input("enter a two digit number. ")

num1 =int(two_digit_num[0])
num2 =int(two_digit_num[1])

result = (num1 + num2)

print(result)
'''

# math operators add(+), minus(-), multiply(*) dived(/) power_to(**) remainder(%)
# pemdaslr is () first, then ** , then *, then /,then +,then -,
# eg 1
'''
print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
'''

# ex 2
'''
weight = input("please enter your weight in kg ")
Height = input("please enter your height in meters ")

bmi = (int(weight) / float(Height) **2)

BMI = int(bmi)

print("your BMI is " + str(BMI))
'''

# eg 3 
# how to round a number
'''
print(round(8 / 3)) 
'''
#how to round a number to it's nearest decimal point 
'''
print(round(8 / 3, 2))
'''

# this is how to get an int from division without converting it
'''
print(8 // 3)
'''

# f strings
'''
score = 5
height = 1.8
is_Win = True

print(f"your score is {score}, your height is {height}, you are wining is {is_Win} " )
'''

# ex 3
'''
age = (input("enter your age "))

age_as_int = int(age)

years_left = 90 - age_as_int
days_left = years_left * 365
week_left = years_left * 52
months_left = years_left * 12

print(f"if you live till 90 you have {years_left} years left ,{months_left} months left, {week_left} weeks left , and {days_left} days left.")
'''


# tip calculator 
# this will calculate your total bill with tip and split it evenly between you and your friends at a restaurant 
print("welcome to  your tip calculator ")
bill = float(input("what was your total bill "))
tip = int(input("please enter your percentage , entre 10, 12, 15 "))
people = int(input("how many people are splitting the bill " ))

bill_with_tip = round(tip / 100 * bill + bill)
bill_by_people = round(bill_with_tip / people)

print(f"your total bill with tip is  {bill_with_tip}")
print(f"you each pay {bill_by_people}")
