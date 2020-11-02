# exercise-3-15.py
# A program to approximate the value of pi by summing the terms of a series

import math

def main():
    print("This program approximates the value of pi by summing the terms of a series.")
    n = eval(input("How many numbers of terms to sum: "))
    sum = 0
    m = 1
    for i in range(1, 2 * n + 1, 2):
        sum = sum + 4 / i * m
        m = m * -1
    print("The sum of the", n, "terms is", sum)
    print("The difference to pi is", math.pi - sum)
    
main()