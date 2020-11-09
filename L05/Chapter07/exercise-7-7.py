# exercise-7-7.py
# A program to calculate a babysitting bill

def main():

    print("This program calculates a babysitting bill.")
    startTime = input("Enter the start time in [hh:mm]: ")
    endTime = input("Enter the end time in [hh:mm]: ")

    startHrs = eval(startTime[:len(startTime)-3])
    starMin = eval(startTime[-2:len(startTime)])
    endHrs = eval(endTime[:len(endTime)-3])
    endMin = eval(endTime[-2:len(endTime)])

    startTime = startHrs + starMin / 60
    endTime = endHrs + endMin / 60

    time = endTime - startTime

    if endTime > 21:
        lateTime = endTime - 21
        bill = (time - lateTime) * 2.5 + lateTime * 1.75
    else: 
        bill = time * 2.5

    print("The total babysitting bill is ${0}.".format(bill))

main()