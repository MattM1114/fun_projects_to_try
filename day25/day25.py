"""with open("weather_data.csv") as data_file:
    data_ = data_file.readlines()
    print(data_)"""
# or the on below which is  better than now I will take each temperature and turn it into a string 
"""
import csv

with open("weather_data.csv") as data_file:
    temperature  = []
    data_ = csv.reader(data_file)
    for row in data_:
        print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)
"""
# here we will learn about pandas which is not 
# inbuilt so you will have to type
# "pip install pandas into your "command line aka terminal
# to do the same thing but cleaner and with less code
import pandas  

"""
data =pandas.read_csv("weather_data.csv")
print(data) 
print(data["temp"])
"""
# here I am doing a type check with this panda data

data =pandas.read_csv("weather_data.csv")
print(type(data)) 
print(type(data["temp"])) 

# this will tell us that our data file for the weather is is a data frames  
# which is like a table   
# when you type check the second part it will be shown as a series which is a list and 
# also can be considered a single colum in an excel file aka a csv file
# here I will convert the data file to a dict

data_dict = data.to_dict()
print(data_dict)

# below were are turning the temps into there own popper python list 

temp_list = data["temp"].to_list()
print(temp_list)

def average_temp(lst):
    """this will figure out the average of a list of number 
    ,but here I am using it for a list of numbers """
    return (sum(lst)/len(lst))

print(average_temp(temp_list))
# so here is the list [12, 14, 15, 14, 21, 22, 24]
# and the average is 17.4
# or instead of creating this function you can  do this bellow 
print(data["temp"].mean())

# to get the max value which is 24 

print(data["temp"].max())
# or 
print(data.temp.max())

# to get data in a row
print(data[data.day == "Monday"])

# ex
print(data[data.temp == 24])
# it was sunday
# if you did not know the max temp
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32

print(monday_temp_f)

# to create a dataframe from scratch
data_dict = {"students":["Amy", "James", "Angela"],"score":[76,56,65]}
data2 = pandas.DataFrame(data_dict)
data2.to_csv("new_data.csv")
