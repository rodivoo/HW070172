# exercise-5-3.py
# Converts an exam score to the corresponding grade
 
def main():
 
    number = int(input("Enter an exam grade (0-100): "))

    grades = 60 * "F" + 10 * "D" + 10 * "C" + 10 * "B" + 11 * "A"

    print("The corresponding grade is", grades[number])

main()