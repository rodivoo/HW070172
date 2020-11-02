# exercise-5-10.py
# Calculates the average word length in a sentence
 
def main():
 
    print("This program calculates the average word length in a sentence.")

    sentence = input("Enter a sentence: ")
    count = 0

    for i in sentence.split():
        count = count + len(i)

    print("The average word length in this sentence ist", count / len(sentence.split()))

main()
