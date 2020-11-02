# exercise-5-8.py
# Encode and decode Caesar ciphers width circular shift
 
def main():
 
    print("This program encodes and decodes Caesar ciphers.")

    message = input("Enter a message: ")
    message = message.lower()
    key = int(input("Enter a key: "))

    alphStr = "abcdefghijklmnopqrstuvwxyz"
    value = ""

    for ch in message:
        value = value + alphStr[((ord(ch) - 97) + key) % 26]

    print("The encoded or decoded message is", value + ".")

main()