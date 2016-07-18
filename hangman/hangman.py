#!/usr/bin/env python3

"""Having a go at a very basic hangman program. No gui or anything.

will need to capture the word itself
max guesses
guesses used
letters guessed
letters matched

keep score and allow playing again etc.

maybe allow computer to choose a random word somehow
"""

import random

with open('words.txt', 'r') as f:
    words = f.read().splitlines()

class Round(object):
    """docstring for Round"""
    def __init__(self, player):
        super(Round, self).__init__()
        self.player = player            # the player guessing the word
        self.secretWord = ''
        self.displayWord = ''
        self.maxGuesses = 0
        self.guessesUsed = 0
        self.lettersMatched = 0
        self.won = False                # won by the player: the word was guessed


    def setSecretWord():
        if self.player.type == 'computer':
            try:
                ui = input('Enter a word: ')
                self.secretWord = ui.strip().upper()
            except Exception as e:
                return(e)
        elif self.player.type == 'human':
            self.secretWord = random.choice(words)


    def start():
        i = len(self.secretWord)
        self.maxGuesses = i * 1.1
        self.displayWord = '_' * i

        print('Guess the word in {0} goes or fewer.\n\n'.format(self.maxGuesses))
        print(self.displayWord)


    def getGuessesLeft():
        return self.maxGuesses - self.guessesUsed


    def checkWin():
        if self.lettersMatched == len(secretWord):
            self.won = True


    def guess(ch):
        print('Guess is {0}\n'.format(ch))
        self.guessesUsed += 1
        if ch in self.secretWord:
            # put ch into correct position(s) in self.displayWord
            # line below adapted from http://stackoverflow.com/a/11122355/6409460
            found = [i for i, ltr in enumerate(self.secretWord) if ltr == ch]
            for i in found:
                self.lettersMatched += 1
                self.displayWord[i] = ch
            # display result
            print('Correct! {0} is in the word.\n'.format(ch))
            print('{0} guesses left.\n'.format(self.getGuessesLeft()))
            print(self.displayWord)
        else:
            # can you guess up to maxGuesses or is there also a set number of lives?
            # display result
            print('Oh dear. {0} is not in the word.\n'.format(ch))
            print('{0} guesses left.\n'.format(self.getGuessesLeft()))
            print(self.displayWord)


    def play():
        while self.getGuessesLeft() > 0:
            if not self.checkWin():
                if self.player.type == 'human':
                    ui = input('Guess a letter: '.strip().upper())
                    self.guess(ui)
                elif self.player.type == 'computer':
                    ch = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                    self.guess(ch)
            elif self.checkWin():
                print('Someone won - change this message later to make it better.')
                break

        if self.getGuessesLeft() == 0:
            print('Ran out of guesses guv.')


class Player(object):
    """docstring for Player"""
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.type = ''
        self.score = 0
        self.turn = False

    def setType(s):     # not working so setting type directly in lines 135 and 144
        self.type = s

    def giveType():
        return self.type

    def scorePoint():
        self.score += 1

    def setTurn():
        self.turn = True

    def unsetTurn():
        self.turn = False

    def __str__(self):
        return 'The {0} named {1} has scored {2} points'.format(self.type, self.name, str(self.score))


def getPlayers(l):
    print('This is a game for two players.\nOne of whom is the computer.')
    try:
        ui = input('What should the computer be called? ').strip().title()
        player1 = Player(ui)
        player1.type = 'computer'
        l.append(player1)
    except Exception as e:
        print(e)

    print('OK, and now we need another player...')
    try:
        ui = input('What is your name? ').strip().title()
        player2 = Player(ui)
        player2.type = 'human'
        l.append(player2)
    except Exception as e:
        print(e)


def doRound(i, player):
    i = Round(player)
    if player.turn:
        i.start()
        i.play()
        if i.checkWin:
            player.scorePoint
    elif not player.turn:
        print('Something went wrong, it\'s not {0}\'s turn!'.format(player.name))


def getScores(l):
    for obj in l:
        print(obj)

def main():
    l = []  # this list will store the players throughout the game
    getPlayers(l)

    q = list(l)  # this list controls the order of play

    roundsPlayed = 0

    playerNow = random.choice(q)
    q.pop(q.index(playerNow))
    # next player is now at q(0)

    print('The first player will be {0}'.format(playerNow.name))
    roundsPlayed += 1
    playerNow.setTurn
    doRound(roundsPlayed, playerNow)
    print('Here are the scores after round {0}:'.format(roundsPlayed))
    getScores(l)
    playerNow.unsetTurn
    q.append(playerNow) # player whose turn has just ended is now at q(1)

    while True:
        try:
            ui = input('Play again? ').strip().lower()
            if ui in ('y', 'yes'):
                # play more rounds
                roundsPlayed += 1
                playerNow = q.pop(0)
                playerNow.setTurn
                doRound(roundsPlayed, playerNow)
                print('Here are the scores after round {0}:'.format(roundsPlayed))
                getScores(l)
                playerNow.unsetTurn
                q.append(playerNow) # now at q(1)

            elif ui in ('n', 'no'):
                break
            else:
                print('Please enter yes or no.')
        except Exception as e:
            print(e)

    print('OK, the game is over. The final scores are: ')
    getScores(l)


if __name__ == '__main__':
    print('Welcome to Hangman!')
    main()
