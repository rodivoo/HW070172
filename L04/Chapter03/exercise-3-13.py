# exercise-3-13.py
# A program to sum a series of numbers entered by the user

def main():
    print("This program sums a series of numbers.")
    n = eval(input("How many numbers are to be summed: "))
    sum = 0
    for i in range(n):
        number = eval(input("Enter a number: "))
        sum = sum + number
    print("The total sum of the", n, "numbers is", sum)
    
main()