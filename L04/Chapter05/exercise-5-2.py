# exercise-5-2.py
# Converts a quiz score to the corresponding grade
 
def main():
 
    number = int(input("Enter a grade (0-5): "))

    grades = "FFDCBA"

    print("The corresponding grade is", grades[number])

main()