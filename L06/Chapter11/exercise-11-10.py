# exercise-11-10.py
# A program that uses the sieve algorithm to find all the primes less than or equal to n

def findPrimes(n):
    x = []
    for i in range(2, n+1):
        x.append(i)
    y = []
    while len(x) >= 1:
        y.append(x[0])
        z = []
        for i in x[1:]:
            if i % x[0] != 0:
                z.append(i)
        x = z
    return y

def main():
    print("This program uses the sieve algorithm to find all the primes less than or equal to n.")
    n = int(input("Enter n: "))
    print("Primes less than or equal to", n, "are:")
    print(findPrimes(n))

if __name__ == '__main__': main()