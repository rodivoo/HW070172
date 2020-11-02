# exercise-3-16.py
# A program to compute the nth Fibonacci number

import math

def main():
    print("This program computes the nth Fibonacci number.")
    n = eval(input("Enter n: "))
    a = 0
    b = 1
    for i in range(n-1):
       c = a + b
       a = b
       b = c
    print("The", n, "th Fibonacci number is", b)
    
main()