# exercise-6-13.py

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def main():
    myList = ["1", "2", "3", "4", "5", "6", "7", "8"]
    toNumbers(myList)
    print(myList)

main()