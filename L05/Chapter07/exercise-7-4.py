# exercise-7-4.py
# A program to calculate the class standing from the number of credits
 
def main():
 
    print("This program calculates the class standing from the number of credits.")
    credit = int(input("Enter the number of credits: "))

    if credit >= 26:
        standing = "Senior"
    elif credit >= 16:
        standing = "Junior"
    elif credit >= 7:
        standing = "Sophomore"
    else:
        standing = "Freshman"

    print("The class standing is " + standing + ".")

main()