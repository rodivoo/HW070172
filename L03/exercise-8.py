# exercise-8.py
# A program to compute the value of an investment

def main():
    print("This program calculates the future value of an investment with variable interest periods")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    periods = eval(input("Enter the number of times that the interest is compounded each year: "))
    years = eval(input("Number of years for the investment: "))

    nominalrate = apr / periods

    for i in range(years * periods):
        principal = principal * (1 + nominalrate)

    print("The value in", years, "years is", principal)

main()