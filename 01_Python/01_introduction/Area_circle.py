#Write a Python program which accepts the radius of a circle from the user and compute the area.


# Enter the radius of circle 
Radius = float (input ("Please enter the radius of the circle: "))  


# Function to calculate the area of a circle

def Area_circle(Radius):
    pi = 3.14159
    return pi *(Radius **2)

 # the area  
area_of_the_circle = Area_circle(Radius)

print (f"The area of the given circle with {Radius} is: {area_of_the_circle}")
