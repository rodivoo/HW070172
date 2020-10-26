# exercise-9.py
# A program to convert Fahrenheit temps to Celsius

def main():
    print("This program converts Fahrenheit temperarure to Celsius")
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) * 5/9
    print("The temperature is", celsius, "degrees Celsius.")

main()