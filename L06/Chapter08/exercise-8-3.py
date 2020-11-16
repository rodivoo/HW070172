# exercise-8-3.py
# A program to calculate how long it takes for an investment to double at a given interest rate

def main():
    print("This program calculates how long it takes for an investment to double at a given interest rate.")
    rate = eval(input("Enter the interest rate: "))
    
    investment = 1
    years = 0

    while investment <= 2:
        years = years + 1
        investment = investment * (1 + rate)
    
    print("It takes", years, "years.")

main()