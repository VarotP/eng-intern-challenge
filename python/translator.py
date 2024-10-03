import sys

braille_dict = {
    'a': 'O.....',    'b': 'O.O...',    'c': 'OO....',    'd': 'OO.O..',
    'e': 'O..O..',    'f': 'OOO...',    'g': 'OOOO..',    'h': 'O.OO..',
    'i': '.OO...',    'j': '.OOO..',    'k': 'O...O.',    'l': 'O.O.O.',
    'm': 'OO..O.',    'n': 'OO.OO.',    'o': 'O..OO.',    'p': 'OOO.O.',
    'q': 'OOOOO.',    'r': 'O.OOO.',    's': '.OO.O.',    't': '.OOOO.',
    'u': 'O...OO',    'v': 'O.O.OO',    'w': '.OOO.O',    'x': 'OO..OO',
    'y': 'OO.OOO',    'z': 'O..OOO',    ' ': '......',
    'capital': '.....O',
    'number': '.O.OOO'
}
reverse_braille_dict = {v: k for k, v in braille_dict.items()}

def english_to_braille(text):
    result = []
    number_mode = False

    for char in text:
        if char.isalpha():
            if number_mode:
                result.append(braille_dict[' '])
                number_mode = False
            if char.isupper():
                result.append(braille_dict['capital'])
            result.append(braille_dict[char.lower()])
        # for numbers just add the difference between 'a' and '1'
        elif char.isdigit():
            if not number_mode:
                result.append(braille_dict['number'])
                number_mode = True
            result.append(braille_dict[chr(ord(char) - ord('0') + ord('a') - 1)])
        elif char == ' ':
            result.append(braille_dict[' '])
            number_mode = False
        else:
            print("char: " + char +  " not supported")
            result.append(char)  # Keep non-alphanumeric characters as is

    return ''.join(result)

def braille_to_english(text):
    result = []
    capitalize_next = False
    number_mode = False

    # Ensure Braille string in multiple of 6s
    if len(text) % 6 != 0:
        raise ValueError("Invalid Braille input: length must be a multiple of 6")

    for i in range(0, len(text), 6):
        char = text[i:i+6]
        if char == braille_dict['capital']:
            capitalize_next = True
        elif char == braille_dict['number']:
            number_mode = True
        elif char == braille_dict[' ']:
            result.append(' ')
            number_mode = False
        elif char in reverse_braille_dict:
            if number_mode:
                result.append(str(ord(reverse_braille_dict[char]) - ord('a') + 1))
            else:
                letter = reverse_braille_dict[char]
                if capitalize_next:
                    letter = letter.upper()
                    capitalize_next = False
                result.append(letter)
        else:
            print("char: " + char +  " not supported")
            result.append(char) 

    return ''.join(result)

def is_braille(text):
    valid_chars = set('O.')
    return all(char in valid_chars for char in text)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <text>")
        return

    text = ' '.join(sys.argv[1:])

    if is_braille(text):
        result = braille_to_english(text)
    else:
        result = english_to_braille(text)

    print(result)

if __name__ == "__main__":
    main()