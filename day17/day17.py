# how to create a class  
class User:
    def __init__(self, user_1d , name):
        #print("new user being created ...")
        self.id = user_1d
        self.name = name 
        self.followers = 0
        self.following = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "matt")


print(user_1.name)

user_2 = User(name="Jack",user_1d="002")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers, user_2.following)

# PascalCase - classes
# snake_case  for everything else

# initialize to set values at the begging of a program or subprogram


