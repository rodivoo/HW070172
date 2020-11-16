# exercise-11-11.py
# A program to replace all four-letter words by ****

def main():
    print("This program replaces all four-letter words by ****.")
    infile = open("input-11.txt", "r")
    outfile = open("output-11.txt", "w")
    for line in infile:
        words = line.split()
        for i in range(len(words)):
            if len(words[i]) == 4 and words[i].isalpha():
                words[i] = "****"
        line = " ".join(words)
        print((line), file = outfile)
    infile.close()
    outfile.close()

if __name__ == '__main__': main()