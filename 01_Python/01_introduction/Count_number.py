
# Write a Python program to count the number 4 in a given list.

# Define a function count_number that takes a list of numbers (List_numbers) as a parameter.
def count_number(List_numbers):
# Initialize a variable count to keep the count of occurrences of the number 4.
    count = 0 
# Iterate through each element (number) in the input list .
    for number in List_numbers:
        # Check if the  number is equal to 4.
        if number == 4: 
            # If the element is 4, increment the count by 1. 
            count = count + 1
# return the final count 
    return count

# example list to count number 
List_example = [4,5,9,4,8,13,4]

print(f"count of number 4 is : {count_number(List_example)}")
