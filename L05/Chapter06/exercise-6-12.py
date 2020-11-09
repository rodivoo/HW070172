# exercise-6-12.py

def sumList(nums):
    x = 0
    for i in range(len(nums)):
        x = x + nums[i]
    return x

def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8]
    print(sumList(myList))

main()