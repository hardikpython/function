import math

def calculate_circumference(radius):
    # Circumference of the circle = 2 * pi * radius
    circumference = 2 * math.pi * radius
    return circumference

# Input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the circumference
circumference = calculate_circumference(radius)
print(f"The circumference of the circle with radius {radius} is: {circumference}")
