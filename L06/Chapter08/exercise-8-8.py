# exercise-8-8.py
# A program to find the GCD of two numbers

def main():
    print("This program finds the GCD of two numbers.")
    n = int(input("Enter the first number: "))
    m = int(input("Enter the seconf number: "))
    
    while m > 0:
        h = n % m
        n = m
        m = h
    
    print("The GCD of the two numbers is {0}.".format(n))

main()