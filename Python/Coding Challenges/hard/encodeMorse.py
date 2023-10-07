"""
Project

    Create a function that takes a string as an argument and returns the Morse code equivalent.

Examples

    encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

    encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

Notes

    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    - Ouput should be International Morse Code, and use the standard conventions for symbols not defined inside the ITU recommendation (see Resources).
    - Input value can be lower or upper case.
    - Input string can have digits.
    - Input string can have some special characters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).
    - One space " " is expected after each character, except the last one.

    LINK: https://edabit.com/challenge/5bYXQfpyoithnQisa

Thoughts

    - iterate through input and do a dictionary search. Ideally with a decent search method
    - unsure I can divide and conquer search when my keys are strings

"""
dictionary = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}

def encode_morse(message):
    morseMessage = ""
    message = message.upper()
    for i in message:
        morseMessage += (dictionary.get(i) + " ")
    return(morseMessage[:-1]) # return morseMessage minus the one space at the end


print(encode_morse("test ing 123")) # testing

# completed and test July 17, 2023