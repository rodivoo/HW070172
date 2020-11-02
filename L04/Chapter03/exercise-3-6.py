# exercise-3-6.py
# A program to calculate the slope of a line through two points

def main():
    print("This program calculates the slope of a line through two (non-vertical) points.")
    x1, y1 = eval(input("Enter the coordinates of the first point: "))
    x2, y2 = eval(input("Enter the coordinates of the second point: "))
    slope = (y2 - y1) / (x2 - x1)
    print("The slope of the line is", round(slope,3))
    
main()