# exercise-5.py
# A program to convert Celsius temps to Fahrenheit

def main():
    print("This program prints a table of Celsius temperarure and the Fahrenheit equivalents every 10 degrees from 0°C to 100°C ")
    for i in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]:
        fahrenheit = 9/5 * i + 32
        print(i, fahrenheit)

main()