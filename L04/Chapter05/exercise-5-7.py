# exercise-5-7.py
# Encode and decode Caesar ciphers
 
def main():
 
    print("This program encodes and decodes Caesar ciphers.")

    message = input("Enter a message: ")
    key = int(input("Enter a key: "))

    value = ""

    for ch in message:
        value = value + chr(ord(ch) + key)

    print("The encoded or decoded message is", value + ".")

main()