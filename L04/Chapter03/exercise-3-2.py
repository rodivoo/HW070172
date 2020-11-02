# exercise-3-2.py
# A program to calculate the cost per square inch of a circular pizza

import math

def main():
    print("This program calculates the cost per square inch of a circular pizza")
    diameter = eval(input("What is diameter of the pizza? "))
    price = eval(input("What is price of the pizza? "))
    area = math.pi * (diameter / 2) ** 2
    cost = price / area
    print("A square inch of the pizza costs", round(cost,3))

main()