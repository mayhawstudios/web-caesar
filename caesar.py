import string

def alphabet_position(letter):
    alpha_dict = {}
    letter = letter.lower()

    for n in range(0,26):
        alpha_dict[string.ascii_lowercase[n]] = n
    
    return alpha_dict[letter]


def rotate_character(char, rot):
    capitalize = False

    if char in string.ascii_letters:
        if char.isupper():
            capitalize = True

        char_val = (alphabet_position(char) + rot) % 26

        if capitalize:
            return string.ascii_uppercase[char_val]
        else:
            return string.ascii_lowercase[char_val]
    else:
        return char