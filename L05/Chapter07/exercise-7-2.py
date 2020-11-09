# exercise-7-2.py
# A program to convert a quiz score to the corresponding grade
 
def main():

    print("This program converts a quiz score to the corresponding grade.")
    number = int(input("Enter a grade (0-5): "))

    if number == 5:
        grade = "A"
    elif number == 4:
        grade = "B"
    elif number == 3:
        grade = "C"
    elif number == 2:
        grade = "D"
    elif number == 1 or number == 0:
        grade = "F"

    print("The corresponding grade is " + grade + ".")

main()