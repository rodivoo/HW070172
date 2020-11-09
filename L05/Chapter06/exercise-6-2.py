# exercise-6-2.py
# A program to print the lyrics for the ten verses of "The Ants Go Marching"

def verse(num, activity):
    phrase = "The ants go marching " + num + " by " + num + ","
    print((phrase + " hurrah!" * 2 + "\n") * 2 + phrase)
    print("The little one stops to", activity + ",")
    print("And the all go marching down…\nIn the ground…\nTo get out…\nOf the rain.\n"
            + "Boom! " * 3 + "\n")

def main():
    verse("one", "suck his thumb")
    verse("two", "tie his shoe")
    verse("three", "climb a tree")
    verse("four", "shut the door")
    verse("five", "take a dive")
    verse("six", "pick up sticks")
    verse("seven", "pray to heaven")
    verse("eight", "roller skate")
    verse("nine", "check the time")
    verse("ten", "shout \"The End\"")

main()