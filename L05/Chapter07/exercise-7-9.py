# exercise-7-9.py
# A program to calculate the date of easter in the years 1982-2048

def main():

    print("This program calculates the date of easter in the years 1982-2048.")
    year = int(input("Enter the year: "))
 
    if 1982 <= year <= 2048:
        a = year % 19
        b = year % 4
        c = year % 7
        d = (19 * a + 24) % 30
        e = (2 * b + 4 * c + 6 * d + 5) % 7
        date = 22 + d + e
        if date > 31:
            date = date - 31
            month = "April"
        else:
            month = "March"
        print("The date of easter in that year is " + month + " {0}.".format(date))
    else:
        print("The year ist not in the proper range.")

main()