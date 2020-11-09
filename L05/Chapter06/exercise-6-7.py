# exercise-6-7.py
# A program to compute the nth Fibonacci number

import math

def fibo(n):
    a = 0
    b = 1
    for i in range(n-1):
       c = a + b
       a = b
       b = c
    return b

def main():
    print("This program computes the nth Fibonacci number.")
    num = eval(input("Enter n: "))

    print("The {0}th Fibonacci number is {1}.".format(num, fibo(num)))
    
main()