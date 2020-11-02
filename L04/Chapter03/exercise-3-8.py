# exercise-3-8.py
# A program to calculate the gregorian epact of a specific year

def main():
    print("This program calculates the gregorian epact of a specific year.")
    year = eval(input("Enter a 4-digit year: "))
    C = year // 100
    epact = (8 + (C // 4) - C + ((8 * C + 13) // 25) + 11 * (year % 19)) % 30
    print("The gregorian epact for the year", year, "is" , epact)
    
main()