# exercise-8-2.py
# A program to print a table of windchill values

def main():
    print("This program prints a table of windchill values:")
    print()
    v = -5
    while v <= 50:
        t = -20
        if v == -5:
            print(" "*8, end = " ")
        else:  
            print(format(v, "4"), "mph", end = " ")
        while t <= 60:
            if v == -5:
                print(format(t, "6") + "°F", end = " ")
            elif v == 0:
                print(format(t, "8.1f"), end = " ")
            else:
                windchill = 35.74 + 0.6215 * t - 35.75 * v ** 0.16 + 0.4275 * t * v ** 0.16
                print(format(windchill, "8.1f"), end = " ")
            t = t + 10
        print()
        v = v + 5

main()