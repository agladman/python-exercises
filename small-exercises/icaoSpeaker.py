#!/usr/bin/env Python3

"""The International Civil Aviation Organization (ICAO) alphabet assigns
    code words to the letters of the English alphabet acrophonically
    (Alfa for A, Bravo for B, etc.) so that critical combinations of
    letters (and numbers) can be pronounced and understood by those who
    transmit and receive voice messages by radio or telephone regardless
    of their native language, especially when the safety of navigation
    or persons is essential. Here is a Python dictionary covering one
    version of the ICAO alphabet:

    [ snip - see below ]

    Your task in this exercise is to write a procedure speak_ICAO() able
    to translate any text (i.e. any string) into spoken ICAO words. You
    need to import at least two libraries: os and time. On a mac, you
    have access to the system TTS (Text-To-Speech) as follows:

    os.system('say ' + msg), where msg is the string to be spoken.

    (Under UNIX/Linux and Windows, something similar might exist.) Apart
    from the text to be spoken, your procedure also needs to accept two
    additional parameters: a float indicating the length of the pause
    between each spoken ICAO word, and a float indicating the length of
    the pause between each word spoken.
    """

import os
import time


def speak_ICAO(text, pause1, pause2):
    icaoDict = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta',
                'e': 'echo', 'f': 'foxtrot', 'g': 'golf', 'h': 'hotel',
                'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
                'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa',
                'q': 'quebec', 'r': 'romeo', 's': 'sierra', 't': 'tango',
                'u': 'uniform', 'v': 'victor', 'w': 'whiskey', 'x': 'x-ray',
                'y': 'yankee', 'z': 'zulu'}
    output = []
    wordstring = []
    for ch in text.lower():
        if ch in (' \n'):
            output.append(wordstring)
            pass
        elif ch not in icaoDict.keys():
            pass
        else:
            wordstring.append(icaoDict[ch])

    for wordstring in output:
        for word in wordstring:
            os.system('say ' + word)
            time.sleep(pause1)
        time.sleep(pause2)

while True:
    ui = input('Enter your message: ')
    if ui:
        text = ui
        break
    else:
        print('No message found.')

while True:
    ui = float(input('Enter time to pause between ICAO words: '))
    if isinstance(ui, float):
        pause1 = ui
        break
    else:
        print('Please enter the value correctly.')

while True:
    ui = float(input('Enter time to pause between words in the message: '))
    if isinstance(ui, float):
        pause2 = ui
        break
    else:
        print('Please enter the value correctly.')

speak_ICAO(text, pause1, pause2)
