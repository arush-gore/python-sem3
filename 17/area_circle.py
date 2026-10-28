import math # Import the math module to access the value of pi

# Function to calculate the area of a circle
def calculate_area_circle(radius):
    return math.pi * radius ** 2 # Area of circle = pi * r^2

# Accept radius from the user
radius = float(input("Enter the radius of the circle. "))

# Call the function and display the result
area = calculate_area_circle(radius)
print(f"The area of the circle is: {area}.")