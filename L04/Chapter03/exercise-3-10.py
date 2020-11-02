# exercise-3-10.py
# A program to calculate the required length of a ladder

import math

def main():
    print("This program calculates the required length of a ladder.")
    height = eval(input("Enter the height of the house: "))
    angle = eval(input("Enter the angle of the ladder in degrees: "))
    angle = math.pi / 180 * angle
    length = height / math.sin(angle)
    print("The required length of the ladder is", round(length,3))
    
main()