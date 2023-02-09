# this is a program that test if you get in to heaven or not and this also test how rich you will be in heaven
print("The Heaven Test")

believer = input(
    "Are you a believer in Jesus christ if yes type yes if not type no ")
point_in_fav = 0
point_against = 0


if believer.lower() != "yes":
    print("you have no chance in heaven")
    quit()
else:
    christian = input("Are you a follower of Jesus ")
    if christian.lower() != "yes":
        print("even the demons believe you need to do more")
        quit()
    else:
        loving = input("if you are loving please type y ")
        if loving == 'y':
            point_in_fav = point_in_fav + 1
        else:
            point_against = point_against + 1

        joy = input("if you bring joy to others type y ")
        if joy == 'y':
            point_in_fav = point_in_fav + 1
        else:
            point_against = point_against + 1

        gentle = input('if you are gentle type y ')
        if gentle == 'y':
            point_in_fav = point_in_fav + 1
        else:
            point_against = point_against + 1

        sheep = input('do you bring people towards God if yes type y ')
        if sheep == 'y':
            point_in_fav = point_in_fav + 1
        else:
            point_against = point_against + 1

        self = input('do you have self control if yes type y ')
        if self == 'y':
            point_in_fav = point_in_fav + 1
        else:
            point_against = point_against + 1

        if point_in_fav == 5:
            print("you will be rich in heaven")
        elif point_against == 5:
            print("you need to do more")
