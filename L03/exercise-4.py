# exercise-4.py
# A program to convert Celsius temps to Fahrenheit

def main():
    print("This program converts Celsius temperarure to Fahrenheit")
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()