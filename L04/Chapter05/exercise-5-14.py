# exercise-5-14.py
# A program to calculate the number of lines, words and characters of a file

def main():
    print("This program calculates the number of lines, words and characters of a file.")

    infileName = input("Enter a file name (inputwc.txt): ")
    infile = open(infileName, "r")

    data = infile.read()
    lines = data.split("\n")
    words = data.split()
    characters = data.replace("\n","")

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of charcters:", len(characters))

    infile.close()

main()