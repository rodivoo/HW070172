# exercise-6-6.py
# A program to calculate the area of a triangle

import math

def areaTriangle(a,b,c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s -a) * (s - b) * (s - c))
    return area

def main():
    print("This program calculates the area of a triangle.")
    x, y, z = eval(input("Enter the lengths of its three sides (separated by comma): "))

    print("The area of the triangle is {0:0.2f}.".format(areaTriangle(x,y,z)))
    
main()