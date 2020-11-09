# exercise-6-5.py
# A program to calculate the cost per square inch of a circular pizza

import math

def pizzaArea(z):
    area = math.pi * (z / 2) ** 2
    return area

def pizzaCosts(x,y):
    cost = x / pizzaArea(y)
    return cost

def main():
    print("This program calculates the cost per square inch of a circular pizza")
    diameter = eval(input("What is diameter of the pizza? "))
    price = eval(input("What is price of the pizza? "))

    print("A square inch of the pizza costs {0:0.4f}.".format(pizzaCosts(price, diameter)))

main()