# exercise-5-12.py
# A program to compute the value of an investment

def main():
    print("This program calculates the future value of an investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Number of years for the investment: "))

    print("{0:6} {1:^8}".format("Year", "Value"))
    print("----------------")
    print("{0:^6} €{1:>8.2f}".format(0, principal))

    for i in range(years):
        principal = principal * (1 + apr)
        print("{0:^6} €{1:>8.2f}".format(i+1, principal))

main()