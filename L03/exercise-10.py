# exercise-10.py
# A program to convert distances measured in kilometers to miles

def main():
    print("This program converts distances measured in kilometers to miles")
    kilometers = eval(input("What is the distances in kilometers? "))
    miles = kilometers * 0.62
    print("The distance is", miles, "miles.")

main()