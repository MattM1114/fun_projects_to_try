# if ,elif, else, and , not , or
# eg 0 this checks if you are tall enough for a ride based on cm
'''
print("welcome to the rollercoaster ")
height = int(input("What is your height in cm? "))

if height >= 120 :
	print("you are tall enough to go on this ride , congrats.")
else:
	print("sorry you can't go on this ride, your not tall enough.")
'''
# ex 0 this checks if a number is odd or even
'''
num = int(input("Please enter a number "))
if num % 2 == 0 :
	print("even")
else:
	print("odd")
'''
# eg 1 this this will check your height , then check how much you have to pay depending on your age
'''
print("welcome to the rollercoaster ")

height = int(input("What is your height in cm? "))
age = int(input("please enter your age "))

if height >= 120:
	print("you are tall enough to go on this ride , congrats.")
	if age < 12:
		print("You're a child, you have to pay 5 $ for this ride")
	elif age <= 18:
		print("You're a teen, you have to pay 7 $ for the ride")
	else:
		print("You're an adult, you have to pay 12 $ for this ride")
else:
	print("sorry you can't go on this ride, your not tall enough.")
'''
# ex 1 this will check your BMI and tell you if you are within the the right weight for your height in m and kg
'''
weight = input("please enter your weight in kg ")
Height = input("please enter your height in meters ")

BMI = round(float(weight) / float(Height) ** 2)

if BMI < 18:
	print(f"you are underweight, your BMI is {BMI}")
elif BMI <= 25:
	print(f"you have a heathy BMI, your BMI is {BMI}")
else:
	print(f"you are overweight,your BMI is {BMI}")
'''

# ex 2 this will check if it is a leap year or not
year = int(input("Please enter a year "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("it is a leap year")
        else:
            print("it is not a leap year")
    else:
        print("it is a leap year")
else:
    print("it is not a leap year")
