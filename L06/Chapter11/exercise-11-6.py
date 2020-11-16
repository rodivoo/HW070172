# exercise-11-6.py
# A program to scramble a list in a random order

from random import random

def shuffle(myList):
    newList = []
    for i in range(len(myList)):
        x = int(random() * len(myList)) - 1 
        newList.append(myList[x])
        myList.remove(myList[x])
    return newList

def main():
    myList = [3, 1, 6, 9, 4, 8, 2, 4]
    print(myList)
    print("Shuffle:", shuffle(myList))

if __name__ == '__main__': main()