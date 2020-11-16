# exercise-11-5.py

def count(myList, x):
    total = 0
    for i in myList:
        if i == x:
            total = total + 1
    return total

def isin(myList, x):
    for i in myList:
        if i == x:
            return True

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i

def reverse(myList):
    newList = []
    for i in range(len(myList)):
        x = myList[-1 * (i + 1)]
        newList.append(x)
    return newList
        
def sort(myList):
    newList = []
    for i in range(len(myList)):
        x = min(myList)
        newList.append(x)
        myList.remove(x)
    return newList 

def main():
    myList = [3, 1, 6, 9, 4, 8, 2, 4]
    x = 4
    print(myList)
    print("x =", x)
    print("count(myList, x):", count(myList, x))
    print("isin(myList, x):", isin(myList, x))
    print("index(myList, x):", index(myList, x))
    print("reverse(myList):", reverse(myList))
    print("sort(myList):", sort(myList))

if __name__ == '__main__': main()