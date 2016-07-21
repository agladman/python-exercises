# Write a program that automatically converts English text to Morse code and vice versa.

code = {
    'A': '.-', 'B': '-...', 'C': '-.-.',
    'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ' ': '/', '.': '.-.-.-', ',': '--..--',
    ':': '---...', '?': '..--..', "'": '.----.',
    '-': '-....-', '/' :'-..-.', '@' : '.--.-.',
    '=': '-...-', '(': '-.--.', ')': '-.--.-',
    '+': '.-.-.'
}

codeReversed = { v:k for k, v in code.items() }

print('Enter message to encode or decode: ')
source = str(input())

def toMorse(s):
    return ' '.join(code.get(i.upper()) for i in s)

def fromMorse(s):
    return ''.join(codeReversed.get(i) for i in s.split())

isMorse = set('.-/ ')
if set(source).issubset(isMorse):
    print(fromMorse(source))
else:
    print(toMorse(source))
