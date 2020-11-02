# exercise-3-7.py
# A program to calculate the distance between two points

import math

def main():
    print("This program calculates the distance between two points.")
    x1, y1 = eval(input("Enter the coordinates of the first point: "))
    x2, y2 = eval(input("Enter the coordinates of the second point: "))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print("The distance between the two points is", round(distance,3))
    
main()