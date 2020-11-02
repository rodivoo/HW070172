# exercise-3-3.py
# A program to calculate the molecular weight of a carbohydrate


def main():
    print("This program calculates the molecular weight of a carbohydrate.")
    hydrogen = eval(input("What is number of hydrogen atoms? "))
    carbon = eval(input("What is number of carbon atoms? "))
    oxygen = eval(input("What is number of oxygen atoms? "))
    weight = 1.00794 * hydrogen + 12.0107 * carbon + 15.9994 * oxygen
    print("The molecular weight ist", round(weight,3), "grams/mole.")

main()