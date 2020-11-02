# exercise-5-13.py
# A program to compute the value of an investment from a file

def main():
    print("This program calculates the future value of an investment from a file")

    infileName = "inputfutval.txt"
    outfileName = "outputfutval.txt"
    
    infile = open(infileName, "r")
    outfile = open(outfileName, "w")

    principal, apr, years = infile.read().split()

    principal = float(principal)
    apr = float(apr)
    years = int(years)

    print("{0:6} {1:^7}".format("Year", "Value"), file = outfile)
    print("---------------", file = outfile)
    print("{0:^6} €{1:>7.2f}".format(0, principal), file = outfile)

    for i in range(years):
        principal = principal * (1 + apr)
        print("{0:^6} €{1:>7.2f}".format(i+1, principal), file = outfile)

    infile.close()
    outfile.close()

main()