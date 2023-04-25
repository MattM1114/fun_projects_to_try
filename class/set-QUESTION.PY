
# Create a list of numbers with some duplicates
numbers = [1, 2, 3, 2, 4, 5, 3]

# Convert the list to a set to remove duplicates
unique_numbers = set(numbers)

# Print the original list and the set of unique numbers
print("Original list:", numbers)
print("Set of unique numbers:", unique_numbers)

# Create two sets of numbers
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Perform some set operations
union = set1.union(set2)  # combine the sets, removing duplicates
intersection = set1.intersection(set2)  # find the common elements between the sets
difference = set1.difference(set2)  # find the elements in set1 that are not in set2

# Print the results of the set operations
print("Union of set1 and set2:", union)
print("Intersection of set1 and set2:", intersection)
print("Difference of set1 and set2:", difference)

# Check if a number is in the set
if 3 in set1:
    print("3 is in set1")
else:
    print("3 is not in set1")
