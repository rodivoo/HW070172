# exercise-11-8.py
# A program to remove duplicate values form a list

def removeDuplicates(myList):
    for x in myList:
        if myList.count(x) > 1:
            myList.remove(x)
    return myList

def main():
    myList = [3, 1, 1, 6, 5, 8, 3, 9, 3, 3]
    print("This program removes duplicate values form a list.")
    print(myList)
    print("Without duplicate values:", removeDuplicates(myList))

if __name__ == '__main__': main()