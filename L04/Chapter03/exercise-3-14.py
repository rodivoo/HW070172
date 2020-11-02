# exercise-3-14.py
# A program to find the average of a series of numbers entered by the user

def main():
    print("This program finds the average of a series of numbers.")
    n = eval(input("How many numbers are there: "))
    sum = 0
    for i in range(n):
        number = eval(input("Enter a number: "))
        sum = float(sum) + float(number)
    print("The average of the", n, "numbers is", sum / n)
    
main()