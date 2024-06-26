# Write a python program to access environment variables.

import os

variable_name = 'PATH'

path_value = os.environ[variable_name]

print(f"The value of the {variable_name} environment variable is: {path_value}")

'''
import os

def get_environment_variable(variable_name):
    return os.environ.get(variable_name)

# Example usage
variable_name = 'PATH'
path_value = get_environment_variable(variable_name)
print(f"The value of the {variable_name} environment variable is: {path_value}")

'''
