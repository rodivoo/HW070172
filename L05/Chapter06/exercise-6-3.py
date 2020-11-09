# exercise-6-3.py
# A program to calculate the volume and the surface area of a sphere

import math

def sphereArea(radius):
    surface = 4 * math.pi * radius ** 2
    return surface

def sphereVolume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume

def main():
    print("This program calculates the volume and the surface area of a sphere")
    r = eval(input("What is the radius of the sphere? "))
    
    print("The volume of the sphere is", round(sphereVolume(r), 2), "and the surface area is", round(sphereArea(r), 2))

main()