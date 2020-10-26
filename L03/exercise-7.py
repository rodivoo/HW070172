# exercise-7.py
# A program to compute the value of an investment

def main():
    print("This program calculates the future value of an investment plan")

    investment = eval(input("Enter the amount to invest each year: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Number of years for the investment: "))
    principal = 0

    for i in range(years):
        principal = (principal + investment) * (1 + apr)

    print("The value in", years, "years is", principal)

main()