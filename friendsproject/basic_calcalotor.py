#here we will take in input from the user
num1=float(input("enter the 1st number: "))
operator=input("enter the operator,it can be +,-,*,/, **, //, or %: ")
num2=float(input("enter the 2nd number: "))

# here is where we actually do the math
# ans is the answer 

if operator == "+":
    ans = num1 + num2
    print(f"{num1} {operator} {num2} = {ans}") # this is a f string which will show the answer
elif operator == "-":
    ans = num1 - num2
    print(f"{num1} {operator} {num2} = {ans}")
elif operator == "*":
    ans = num1 * num2
    print(f"{num1} {operator} {num2} = {ans}")
elif operator == "/":
    ans = num1 / num2
    print(f"{num1} {operator} {num2} = {ans}")
elif operator == "**":
    ans = num1 ** num2
    print(f"{num1} {operator} {num2} = {ans}")
elif operator == "//":
    ans = num1 // num2
    print(f"{num1} {operator} {num2} = {ans}")
elif operator == "%":
    ans = num1 % num2
    print(f"{num1} {operator} {num2} = {ans}")