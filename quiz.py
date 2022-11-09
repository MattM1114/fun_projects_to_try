# this welcomes people to my game and then asks if they want to play

print('welcome to my computer quiz')

playing = input("Do you want to play? ")
print(playing)

if playing.lower() != "yes":
    quit()

print("okay! let's play :)")
score = 0
# these are the qustions and the answer to them  
# .lower makes things lower case
# score counts the points

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('correct!')
    score += 1
else:
    print('wrong!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('wrong!')

answer = input("what does RAM stand for? ")
if answer.lower() == "random access memory":
    print('correct!')
    score += 1
else:
    print('wrong!')

answer = input("what does psu stand for? ")
if answer.lower() == "power supply":
    print('correct!')
    score += 1
else:
    print('wrong!')
# str() changes things into a string 
print("You got " + str(score) + " questions correct!")