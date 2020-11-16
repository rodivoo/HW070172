# exercise-8-4.py
# A program to print the Syracuse sequence for a starting value

def main():
    print("This program prints the Syracuse sequence for a starting value.")
    starting = int(input("Enter the starting number: "))

    print(starting, end=" ")
    
    while starting != 1:
        if starting % 2 == 0:
            starting = starting / 2
        else:
            starting = starting * 3 + 1
        print(int(starting), end=" ")

    print()

main()