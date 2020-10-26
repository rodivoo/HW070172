# exercise-6.py
# A program to compute the value of an investment

def main():
    print("This program calculates the future value of an investment")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Number of years for the investment: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in", years, "years is", principal)

main()