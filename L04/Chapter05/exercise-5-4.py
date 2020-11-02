# exercise-5-4.py
# Converts a phrase to an acronym
 
def main():
 
    phrase = input("Enter a phrase: ")
    acronym = ""

    for i in phrase.split():
        acronym = acronym + (i[0].upper())

    print("The acronym is", acronym + ".")

main()