# exercise-6-4.py
# A program to calculate the sum and the sum of the cubes of the first n natural numbers

import math

def sumN(n):
    x = 0
    for i in range(1,n+1):
        x = x + i
    return x

def sumNCubes(n):
    y = 0
    for i in range(1,n+1):
        y = y + i ** 3
    return y

def main():
    print("This program calculates the sum and the sum of the cubes of the first n natural numbers")

    num = eval(input("Enter a natural number: "))
    
    print("The sum of the first", num, "natural numbers is", sumN(num), "and the sum of the cubes is", sumNCubes(num))

main()