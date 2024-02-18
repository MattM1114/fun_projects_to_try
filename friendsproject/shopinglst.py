
current_price = 0
number_of_items = 0

while True:
#this loop will ask the user to enter the price of the item and will add it to the current price and add one to the number of items
    i = float(input("please enter the price of the item: "))
    if i <= 0.00:
        print("please enter a valid price")
    elif i > 0.00:
        i += current_price
        number_of_items += 1
        print("the current price is: ",round(i, 2) )
        print("the number of items is: ", number_of_items)
        y = input("would you like to add another item?")
        if y.lower() == "y":
            continue
        else:
            if number_of_items == 1:
                tax  = number_of_items * 0.14
                total = i + tax
                print("the tax is: ", tax)
                print("the total is + tax: ", round(total, 2))
                print("the total is: ", round(i, 2))
                break
            else:
                tax = i * 0.14
                total = i + tax
                print("the tax is: ", tax)
                print("the total is + tax: ", round(total, 2))
                print("the total is: ", round(i, 2))
                break
            