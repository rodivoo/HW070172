# exercise-6-11.py

def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

def main():
    myList = [1, 2, 3, 4, 5, 6, 7, 8]
    squareEach(myList)
    print(myList)

main()