#this is how you open a file in python and read it
"""
file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()
"""
# or
"""
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)
    file.close()
"""
#this is how you open a file in python and write to it "w" = write 
"""
with open ("my_file.txt", mode = "w") as file:
    file.write("new txt.")
"""

# this is how you would add to the file with out deleting what is already there  "a" = append
"""
with open ("my_file.txt", mode = "a") as file:
    file.write("\nnew txt.")
"""

# you can also create a new file in the same as the write mode like this 
"""
with open ("new_file.txt", mode = "w") as file:
    file.write("new txt.")
"""
# this only works when the file does exists and when the open method aka function is in write mode 

# this how you locate a file when it is not in the same file 
"""
with open("C:/Users/User/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
    file.close()
"""

# ex1 
""""
with open("../../Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)
"""