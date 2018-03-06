#!/usr/bin/env python3


while True:
    name = input('What is your name? ')
    if name.replace(' ', '').isalpha():
        print(f'Hello, {name}.')
        break
    else:
        print('That\'s not a name!')

print('Here are the letters in your name: ', end='')
letters = []
for c in name:
    if c not in letters:
        letters.append(c)
letters.sort()
print(', '.join(l for l in letters))

bennychoice = input('Are you a benny tied to a tree? ')
if bennychoice.lower() == 'yes':
    print('Haha, you\'re a benny tied to a tree!')
elif bennychoice.lower() == 'no':
    print('BENNY ON THE LOOSE! BENNY ON THE LOOSE!')
else:
    print('Pfeh.')

