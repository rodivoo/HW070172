# exercise-6-1.py
# A program to print the lyrics of the sing "Old MacDonald" with 5 different animals

def old():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def verse(animal, sound):
    old()
    print("And on the farm he had a", animal + ", Ee-igh, Ee-igh, Oh!")
    print("With a", sound + ",", sound, "here and a", sound + ",", sound, "there.")
    print("Here a", sound + ", there a", sound + ", everywhere a", sound + ",", sound + ".")
    old()
    print()

def main():
    verse("cow", "moo")
    verse("cat", "meow")
    verse("hen", "cluck")
    verse("duck", "quack")
    verse("goat", "baa")

main()