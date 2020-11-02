# exercise-5-6.py
# Calculates the numeric value of a complete name
 
def main():
 
    print("This program calculates the numeric value of a complete name.")

    name = input("Enter a complete name: ")
    name = name.lower().replace(" ", "").replace(".", "")
    value = 0

    for ch in name:
        value = value + ord(ch) - 96

    print("The numeric value is", value)

main()