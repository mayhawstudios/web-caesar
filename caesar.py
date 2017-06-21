import string
from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted_text = ""

    for t in text:
        encrypted_text += rotate_character(t, rot)

    return encrypted_text

def main():
    message = input("Type a message:")
    rotate = int(input("Rotate by:"))

    print(encrypt(message, rotate))

if __name__ == "__main__":
    main()