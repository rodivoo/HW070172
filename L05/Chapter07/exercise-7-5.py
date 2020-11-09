# exercise-7-5.py
# A program to calculate the BMI

def main():

    print("This program calculates the BMI.")
    weight = eval(input("Enter the weight in [kg]: "))
    size = eval(input("Enter the size in [m]: "))

    bmi = weight / size ** 2

    if bmi > 25:
        message = "above"
    elif bmi >= 19:
        message = "within"
    else:
        message = "below"

    print("The BMI is " + message + " the healthy range.")

main()