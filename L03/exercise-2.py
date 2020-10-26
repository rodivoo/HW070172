# exercise-2.py
# A program to convert Celsius temps to Fahrenheit

def main():
    print("This program converts Celsius temperarure to Fahrenheit")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

    input("Press the <Enter> key to quit.")

main()