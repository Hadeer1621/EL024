# Just check all methods of string 
Str_variable = " Hello and welcome in embedded linux dioplama "
print("#==================capitalize===============#")
print(Str_variable.capitalize())
print("#=============title====================#")
print(Str_variable.title())
print("#==============casefold===================#")
print(Str_variable.casefold())
print("#===============center==================#")
Str_variable_0 = "Embededded"
print(Str_variable_0.center(15))  # Spaces
print(Str_variable_0.center(15, "#"))  # Hashes
print("#==============count===================#")
Str_variable_1 = " i love python and learn python then take test of python exam "
print(Str_variable_1.count("python"))
print("#============swapcase=====================#")
print(Str_variable.swapcase()) 
print(Str_variable_1.swapcase())
print("#==============split===================#")
print(Str_variable.split()) # convert to list  ( ) consider empty the space is element 
print("#===============strip==================#")
print(Str_variable_1.strip()) # 
print(Str_variable.rstrip()) # remove spsce from right 
print("#==============just===================#")
# rjust(Width, Fill Char) ljust(Width, Fill Char) used to write any element 
Str_variable_4 = "pyhton"
print(Str_variable_4.rjust(10))
print(Str_variable_4.ljust(10, "#"))
print("#==============upper===================#")
Str_variable_2 = "linux"
print(Str_variable_2.upper())
print("#=================================#")

