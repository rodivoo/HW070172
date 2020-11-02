# exercise-3-4.py
# A program to calculate the distance to a lightning strike


def main():
    print("This program calculates the distance to a lightniung strike.")
    time = eval(input("What is the time elapsed between the flash and the sound of thounder? "))
    distance = 1100 * time / 5280
    print("The distance to the lightniung strike is", round(distance,3), "miles.")

main()