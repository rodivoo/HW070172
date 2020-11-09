# exercise-7-8.py
# A program to calculate the eligibility of a person for the Senate and House

def main():

    print("This program calculates the eligibility of a person for the Senate and House.")
    age = int(input("Enter the perons's age: "))
    citizenship = int(input("Enter the years of citizenship: "))

    if age >= 25 and citizenship >= 7:
        if age >= 30 and citizenship >= 9: 
            print("The person has the eligibility for the Senate and House.")
        else:
            print("The person has the eligibility for the House.")
    else:
        print("The person has no eligibility.")

main()