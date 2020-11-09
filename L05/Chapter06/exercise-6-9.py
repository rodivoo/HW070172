# exercise-6-9.py
# Converts an exam score to the corresponding grade

def grade(score):
    grades = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 11 * "A"
    return grades[score]

def main():
    number = int(input("Enter an exam grade (0-100): "))
    print("The corresponding grade is {0}.".format(grade(number)))

main()