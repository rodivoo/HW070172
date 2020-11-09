# exercise-7-6.py
# A program to calculate a fine

def main():

    print("This program calculates a fine.")
    speedLimit = eval(input("Enter the speed limit in [mph]: "))
    clockedSpeed = eval(input("Enter the clocked speed in [mph]: "))

    if clockedSpeed > speedLimit:
        fine = 50 + (clockedSpeed - speedLimit) * 5
        if clockedSpeed > 90:
            fine = fine + 200
        print("The amount of the fine is ${0}.".format(fine))
    else:
        print("The speed was legal.")

main()