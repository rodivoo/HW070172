# exercise-6-14.py

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def sumList(nums):
    x = 0
    for i in range(len(nums)):
        x = x + nums[i]
    return x

def main():
    infileName = input("Enter a file name (input-6-14.txt): ")
    infile = open(infileName, "r")

    myList = []
    for line in infile.readlines():
        myList.append(line.replace("\n", ""))
    
    toNumbers(myList)
    squareEach(myList)
    
    print("The sum of the squares of the values in the file is {0}.".format(sumList(myList)))

main()