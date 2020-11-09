# exercise-6-10.py
# Converts a phrase to an acronym
 
def acronym(phrase):
    acro = ""
    for i in phrase.split():
        acro = acro + (i[0].upper())
    return acro

def main():
    phrase = input("Enter a phrase: ")
    print("The acronym is", acronym(phrase) + ".")

main()