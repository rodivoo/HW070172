# exercise-3-16.py
# A program to guess the square root of x by Newton's method

import math

def main():
    print("This program guesses the square root of x by Newton's method.")
    x = eval(input("Enter x: "))
    n = eval(input("Enter the number of times to improve the guess: "))
    guess = x / 2
    for i in range(n):
        guess = (guess + x / guess) / 2
    print("The final value of guess is", guess)
    print("The difference between the square root of x and the guess is", math.sqrt(x) - guess)
    
main()