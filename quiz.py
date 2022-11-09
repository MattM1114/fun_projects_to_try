#this welcomes people to my game and then asks if they want to play

print('welcome to my computer quiz')

playing = input("Do you want to play? ")
print(playing)

if playing != "yes":
    quit()

print("okay! let's play :)")

#these are the qustions and the answer to them  
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('correct!')
else:
    print('wrong!')

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('correct!')
else:
    print('wrong!')

answer = input("what does RAM stand for? ")
if answer == "random acesse ":
    print('correct!')
else:
    print('wrong!')

    answer = input("")
if answer == "":
    print('correct!')
else:
    print('wrong!')