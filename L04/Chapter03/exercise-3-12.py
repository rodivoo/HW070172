# exercise-3-12.py
# A program to find the sum of the cubes of the first n natural numbers

def main():
    print("This program finds the sum of the cubes of the first n natural numbers.")
    n = eval(input("Enter the value of n: "))
    sum = 0
    for i in range(1,n+1):
        sum = sum + i ** 3
    print("The sum of the cubes of the first", n, "natural numbers is", sum)
    
main()