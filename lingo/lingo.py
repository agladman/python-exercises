#!/usr/bin/env Python3

"""In a game of Lingo, there is a hidden word, five characters long.
    The object of the game is to find this word by guessing, and in
    return receive two kinds of clues: 1) the characters that are fully
    correct, with respect to identity as well as to position, and 2) the
    characters that are indeed present in the word, but which are placed
    in the wrong position. Write a program with which one can play
    Lingo. Use square brackets to mark characters correct in the sense
    of 1), and ordinary parentheses to mark characters correct in the
    sense of 2). Assuming, for example, that the program conceals the
    word "tiger", you should be able to interact with it in the
    following way:

    >>> import lingo
    snake
    Clue: snak(e)
    fiest
    Clue: f[i](e)s(t)
    times
    Clue: [t][i]m[e]s
    tiger
    Clue: [t][i][g][e][r]
    """

import os
import random

with open('words.txt', 'r') as f:
    words = f.read().split()


class LingoRound(object):
    """represents one iteraton of the lingo game"""

    def __init__(self):
        self.secret_word = ''
        self.won = False

    def cleanWord(self, word):
        output = filter(str.isalpha, word)
        return ''.join(output)

    def setSecretWord(self):
        while True:
            candidate = self.cleanWord(random.choice(words).lower())
            if len(candidate) == 5:
                self.secretWord = candidate
                break
            else:
                # logging.debug('candidate word from computer was too short.')
                pass

    def guess(self, word):
        chars = list(word)
        matched = 0
        for ch in word:
            if ch in self.secret_word:
                if word.index(ch) == self.secret_word.index(ch):
                    chars[word.index(ch)] = '[{0}]'.format(ch)
                    matched += 1
                else:
                    i = chars.index(ch)
                    chars[i] = '({0})'.format(ch)
        output = ''.join(chars)
        # could use len(self.secretWord) below but we know explicit value will
        # be 5
        if matched == 5:
            self.won = True
        return output


class Player(object):
    """holds the player's name, score and number of rounds played"""

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rounds_played = 0


def showRules():
    print("""
        The computer will choose a random word that's five letters long.
        You have to guess this word. Each time you guess, your chosen
        word will be returned with two types of clues included in it.

        1) If a letter in your guess is also in the secret word, but in
        a different position, it will be marked in parentheses.

        2) If a letter in your guess is also in the secret word, and in
        the same position, it will be marked in square brackets.

        For example, if the secret word is "tiger" and you guess "tulip"
        the clue you get back will be "[t]ul(i)p".
        """)


def getScores(player):
    pluraliser = ''
    pluraliser = 's' if player.rounds_played == 1 else pluraliser
    score_string = '\n{0} has played {1} round{2} and scored {3} points.'
    print(score_string.format(player.name,
                              player.rounds_played,
                              pluraliser,
                              player.score))


def playRound(roundnum, player):
    roundnum = LingoRound()
    roundnum.setSecretWord()
    while not roundnum.won:
        ui = input('\nGuess a word or type quit to give up: ').strip().lower()
        if ui == 'quit':
            player.rounds_played += 1
            print('OK, round over. The word was "{0}".'.format(
                roundnum.secretWord))
            break
        elif ui.isalpha():
            if len(ui) == 5:
                clue = roundnum.guess(ui)
                print('Clue: {0}'.format(clue))
            elif len(ui) < 5:
                print('That guess was too short, '
                      'try again with a five-letter word.')
            elif len(ui) > 5:
                print('That guess was too long, '
                      'try again with a five-letter word.')
            else:
                print('I don\'t know what went wrong, but something did.')
                pass
        else:
            print('Invalid guess. Please try a five-letter word.')
    if roundnum.won:
        player.rounds_played += 1
        player.score += 1

# main starts here
print('\n\nWelcome to Lingo!\n\n')

while True:
    ui=input('Would you like to read the rules? ').strip().lower()
    if ui in ('y', 'yes'):
        showRules()
        break
    elif ui in ('n', 'no'):
        break
    else:
        print('Please enter yes or no.')

while True:
    ui=input('What\'s your name? ').strip().title()
    if ui:
        player=Player(ui)
        break
    else:
        Print('Go on, tell me your name.')

i=1
playRound(i, player)
getScores(player)

while True:
    ui=input('\nPlay again? ').strip().lower()
    if ui in ('y', 'yes'):
        i += 1
        playRound(i, player)
        getScores(player)
    elif ui in ('n', 'no'):
        break
    else:
        print('Please enter yes or no.')

print('\nThanks for playing Lingo!\n\n')
