# from p92 in Automate the Boring Stuff with Python

import random

messages = ['It is certain',
    'It is doubtful',
    'Yes, definitely',
    'Reply hazy try again',
    'Ask again later',
    'Concentrate and ask again',
    'My reply is no',
    'Outlook not so good',
    'Very doubtful']

print(messages[random.randint(0, len(messages) -1)])
