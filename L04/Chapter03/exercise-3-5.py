# exercise-3-5.py
# A program to calculate the cost of a coffee order

def main():
    print("This program calculates the cost of a coffee order.")
    pound = eval(input("What is the weight of the coffee order? "))
    cost = 10.50 * pound + 0.86 * pound + 1.50
    print("The cost of the order is", round(cost,3))

main()