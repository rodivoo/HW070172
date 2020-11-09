# exercise-7-3.py
# A program to convert an exam score to the corresponding grade
 
def main():
 
    print("This program converts an exam score to the corresponding grade.")
    number = int(input("Enter an exam grade (0-100): "))

    if number >= 90:
        grade = "A"
    elif number >= 80:
        grade = "B"
    elif number >= 70:
        grade = "C"
    elif number >= 60:
        grade = "D"
    else:
        grade = "E"

    print("The corresponding grade is " + grade + ".")

main()