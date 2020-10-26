# exercise-11.py
# A program to convert pressure measured in psi to bar

def main():
    print("This program converts pressure measured in psi to bar")
    psi = eval(input("What is the pressure in psi? "))
    bar = psi / 14.504
    print("The pressure is", bar, "bar.")

main()