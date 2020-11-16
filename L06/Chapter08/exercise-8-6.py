# exercise-8-6.py
# A program to find every prime number less than or equal to n

def prime(j):
    i = 2
    while i <= j ** 0.5:
        if j % i == 0:
            return
        else:     
            i = i + 1
    print(j) 

def main():
    print("This program finds every prime number less than or equal to n.")
    n = int(input("Enter n: "))

    for i in range(n):
        prime(i+1)

main()