# exercise-8-5.py
# A program to determine if a positive whole number is a prime

def main():
    print("This program determines if a positive whole number is a prime.")
    n = int(input("Enter a number: "))
    
    i = 2
    prime = ""

    while i <= n ** 0.5:
        if n % i == 0:
            prime = "not "
            break
        else:
            i = i + 1   
       
    print("The number", n, "is " + prime + "a prime.")

    

main()