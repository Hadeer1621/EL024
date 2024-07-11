
import sys

# Get the list of command-line arguments
arguments = sys.argv

# Print the command-line arguments
print("Number of arguments:", len(arguments))
print("Arguments:", arguments)

# Print each argument separately
if len(arguments) > 1:
    print("Individual arguments:")
    for i, arg in enumerate(arguments[1:], start=1):
        print(f"Argument {i}: {arg}")
