# exercise-6-8.py
# A program to guess the square root of x by Newton's method

import math

def nextGuess(guess, x):
    guess = (guess + x / guess) / 2
    return guess

def main():
    print("This program guesses the square root of x by Newton's method.")
    x = eval(input("Enter x: "))
    n = eval(input("Enter the number of times to improve the guess: "))
    guess = x / 2
    for i in range(n):
        guess = nextGuess(guess, x)
        
    print("The final value of guess is", guess)
    print("The difference between the square root of x and the guess is", math.sqrt(x) - guess)
    
main()