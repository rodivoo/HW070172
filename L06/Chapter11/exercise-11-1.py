# exercise-11-1.py
# A program to compute mean and standard deviation

import math

def getNumbers():
    nums = []
    xStr = input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x = float(xStr)
        nums.append(x)
        xStr = input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def stdDev(nums, xbar):
    sumDevSq = 0.0
    for num in nums:
        dev = num - xbar
        sumDevSq = sumDevSq + dev * dev
    return math.sqrt(sumDevSq/(len(nums)-1))

def meanStdDev(data):
    xbar = mean(data)
    std = stdDev(data, xbar)
    return xbar, std

def main():
    print("This program computes mean and standard deviation.")

    data = getNumbers()
    xbar = mean(data)
    std = stdDev(data, xbar)
    xbarStd = meanStdDev(data)

    print("\nThe mean is {0:.2f}.".format(xbar))
    print("The standard deviation is {0:.2f}.".format(std))
    print("The mean is {0:.2f} and the standard deviation is {1:.2f}.".format(xbarStd[0], xbarStd[1]))

if __name__ == '__main__': main()

