# exercise-7-1.py
# A program to calculate the total wages for the week

def main():
    print("This program calculates the total wages for the week.")
    hours = eval(input("Enter the number of hours: "))
    rate = eval(input("Enter the hourly rate: "))

    if hours <= 40:
        wage = hours * rate
    else:
        wage = 40 * rate + (hours - 40) * rate * 1.5

    print("The total wages for the week is € {0:0.2f}.".format(wage))

main()