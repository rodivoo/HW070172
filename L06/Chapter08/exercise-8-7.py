# exercise-8-7.py
# A program to find two prime numbers that add up to an even number

def prime(j):
    i = 2
    while i <= j ** 0.5:
        if j % i == 0:
            return False
        else:     
            i = i + 1
    return j

def main():
    print("This program finds two prime numbers that add up to an even number.")

    while True:
        n = int(input("Enter an even number: "))
        if n % 2 == 0:
            print("These following combinations of prime numbers add up to {0}:".format(n))
            break
        print("The number ist not even.")

    x = n - 1
    
    while x >= n / 2:
        if prime(x):
            prime1 = prime(x)
            prime2 = n - prime1
            if prime(prime2):
                print("{0} + {1}".format(prime1, prime2))
        x = x - 1

main()