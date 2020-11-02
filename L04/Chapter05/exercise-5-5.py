# exercise-5-5.py
# Calculates the numeric value of a single name
 
def main():
 
    print("This program calculates the numeric value of a single name.")

    name = input("Enter a single name: ")
    name = name.lower()
    value = 0

    for ch in name:
        value = value + ord(ch) - 96

    print("The numeric value is", value)

main()