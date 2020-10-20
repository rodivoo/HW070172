def main():
    print("With the multiplier 2.0 instead of 3.9 the function converges very quickly to 0.5")
    x = eval(input("Enter a number between 0 und 1: "))
    for i in range(10):
        x = 2.0 * x * (1 - x)
        print(x)

main()