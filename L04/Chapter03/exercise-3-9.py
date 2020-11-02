# exercise-3-9.py
# A program to calculate the area of a triangle

import math

def main():
    print("This program calculates the area of a triangle.")
    a, b, c = eval(input("Enter the lengths of its three sides (separated by comma): "))
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    print("The area of the triangle is", round(area,3))
    
main()