# exercise-3-11.py
# A program to find the sum of the first n natural numbers

def main():
    print("This program finds the sum of the first n natural numbers.")
    n = eval(input("Enter the value of n: "))
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    print("The sum of the first", n, "natural numbers is", sum)
    
main()