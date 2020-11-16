# exercise-8-1.py
# A program to compute the nth Fibonacci number

def main():
    print("This program computes the nth Fibonacci number.")
    n = eval(input("Enter n: "))
    a = 0
    b = 1
    count = 0
    while count < n:
       c = a + b
       a = b
       b = c
       count = count + 1
    print("The {0}th Fibonacci number is {1}.".format(n, b))
    
main()