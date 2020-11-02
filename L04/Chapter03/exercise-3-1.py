# exercise-3-1.py
# A program to calculate the volume and the surface area of a sphere

import math

def main():
    print("This program calculates the volume and the surface area of a sphere")
    radius = eval(input("What is the radius of the sphere? "))
    volume = 4 / 3 * math.pi * radius ** 3
    surface = 4 * math.pi * radius ** 2
    print("The volume of the sphere is", round(volume,2), "and the surface area is", round(surface,2))

main()