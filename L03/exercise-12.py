# exercise-12.py
# A program to print the values of mathematical expressions

def main():
    print("This program calculates the values of mathematical expressions")

    for i in range(100):
        expression = eval(input("Enter a mathematical expression: "))
        print("The value is", expression)

main()