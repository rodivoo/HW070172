# exercise-11-7.py
# A program to compute the inner product of two lists

def innerProd(myListX, myListY):
    total = 0
    for i in range(len(myListX)):
        x = myListX[i] * myListY[i]
        total = total + x
    return total 

def main():
    myListX = [3, 1, 6]
    myListY = [6, 4, 3]
    print("This program computes the inner product of two lists.")
    print("List 1:", myListX)
    print("List 2:", myListY)
    print("The inner product is {0}.".format(innerProd(myListX, myListY)))

if __name__ == '__main__': main()