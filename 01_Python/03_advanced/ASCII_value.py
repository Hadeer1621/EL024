
# Function to get ASCII value of a character
def Get_ASCII(character):
    return ord(character)

# Input character from user
char = input("Enter a character: ")

# Get ASCII value
ascii_value = Get_ASCII(char)

# Print the ASCII value
print(f"The ASCII value of '{char}' is: {ascii_value}")
