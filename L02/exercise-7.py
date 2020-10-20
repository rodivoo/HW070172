def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 und 1: "))
    y = eval(input("Enter a different number between 0 und 1: "))
    n = eval(input("How many numbers should I print: "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x,y)

main()