# Seil Tekinaeva
# March 4, 2026
# Problem 1: Write a function areaOfCircle(r) that returns the area of a circle

import math

def areaOfCircle(r):
    area=math.pi * r * r
    return area
radius = 8
result = areaOfCircle(radius)

print("The area of circle is:", result)
