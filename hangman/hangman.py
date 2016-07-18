#!/usr/bin/env python3

"""Having a go at a very basic hangman program. No gui or anything.
    bug: checkWin does not seem to kick in when the word is guessed.
"""
import datetime
import logging
import random

logging.basicConfig(filename='hangman-{:%Y%m%d-%H%M}.txt'.format(datetime.datetime.now()), level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
# logging.disable(logging.CRITICAL) # comment out this line to enable logging again

# loads words into memory for computer to choose from
with open('words.txt', 'r') as f:
    words = f.read().split()

class Round(object):
    """A Round is one iteration of the game"""
    def __init__(self, player):
        super(Round, self).__init__()
        self.player = player            # the player guessing the word
        self.secretWord = ''
        self.displayWord = ''
        self.maxGuesses = 12
        self.guessesUsed = 0
        self.lettersMatched = 0
        self.won = False                # won by the player: the word was guessed


    def cleanWord(self, word):
        output = []
        for ch in word:
            if ch.isalpha():
                output.append(ch)
        return ''.join(output)


    def setSecretWord(self):
        if self.player.type == 'computer':
            while True:
                try:
                    ui = input('Enter a word, four letters or longer: ')
                    candidate = self.cleanWord(ui.strip().upper())
                    if len(candidate) >= 4:
                        self.secretWord = candidate
                        break
                    else:
                        print('That word is too short.')
                except Exception as e:
                    return(e)
        elif self.player.type == 'human':
            while True:
                candidate = self.cleanWord(random.choice(words).upper())
                if len(candidate) >= 4:
                    self.secretWord = candidate
                    break
                else:
                    logging.debug('candidate word from computer was too short.')
                    pass


    def start(self):
        self.setSecretWord()
        logging.debug('secretWord: {0}'.format(self.secretWord))
        i = len(self.secretWord)
        self.displayWord = '_' * i
        logging.debug('displayWord: {0}'.format(self.displayWord))

        print('Guess the word in {0} goes or fewer.\n\n'.format(self.maxGuesses))
        print(''.join(self.displayWord))


    def getGuessesLeft(self):
        return self.maxGuesses - self.guessesUsed


    def checkWin(self):
        """This does not seem to be working at the moment.
            Not sure if the problem lies in the function itself or in where or how it is being called.
            Possible methods for checking win:
                1. self.lettersMatched == len(self.secretWord) - didn't seem to work
                2. self.displayWord == self.secretWord - testing now
                3. self.secretWord in guessed - not tried yet, would need to pass guessed to the function
            """
        if self.displayWord == self.secretWord:
            self.won = True


    def guess(self, ch):
        if ch in self.secretWord:
            # put ch into correct position(s) in self.displayWord
            # line below adapted from http://stackoverflow.com/a/11122355/6409460
            found = [i for i, ltr in enumerate(self.secretWord) if ltr == ch]
            for i in found:
                self.lettersMatched += 1
                self.displayWord = self.displayWord[:i] + ch + self.displayWord[i + 1:]
                logging.debug('correct guess: {0}'.format(ch))
                logging.debug('guessesUsed: {0} of {1}'.format(self.guessesUsed, self.maxGuesses))
                logging.debug('length of secretWord: {0}; lettersMatched: {1}; displayWord: {2}'.format(len(self.secretWord), self.lettersMatched, self.displayWord))
            # display result
            print('Correct! {0} is in the word.\n'.format(ch))
            print('{0} guesses left.\n'.format(self.getGuessesLeft()))
            print(''.join(self.displayWord))
        else:
            self.guessesUsed += 1   # only increments on incorrect guesses
            logging.debug('incorrect guess: {0}'.format(ch))
            logging.debug('guessesUsed: {0} of {1}'.format(self.guessesUsed, self.maxGuesses))
            print('Oh dear. {0} is not in the word.\n'.format(ch))
            print('{0} guesses left.\n'.format(self.getGuessesLeft()))
            print(''.join(self.displayWord))


    def play(self):
        guessed = []
        while self.getGuessesLeft() > 0:
            if not self.checkWin():
                if self.player.type == 'human':
                    while True:
                        try:
                            ui = input('Guess a letter: ')
                            ch = ui.strip().upper()
                            if ch.isalpha():
                                if ch not in guessed:
                                    self.guess(ch)
                                    guessed.append(ch)
                                    break
                                else:
                                    print('You have already guessed {0}, try again.'.format(ch))
                                    logging.debug('duplicate guess by human')
                            else:
                                print('Only letters will be accepted.')
                                logging.debug('rejected non-alpha guess by human')
                        except Exception as e:
                            print(e)
                            logging.debug('Exception capturing human guess: {0}'.format(e))

                elif self.player.type == 'computer':
                    while True:
                        ch = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
                        if ch not in guessed:
                            self.guess(ch)
                            guessed.append(ch)
                            break
                        else:
                            logging.debug('duplicate guess by computer')
                            pass
            elif self.checkWin():
                print('Someone won - change this message later to make it better.')
                break
        if self.getGuessesLeft() == 0:
            print('Ran out of guesses guv.\nThe Word was {0}'.format(self.secretWord))
            logging.debug('maxGuesses reached')


class Player(object):
    """The Player objects hold the name and type of each player in the game as well as the score.
        Printing the scores is done by calling the string function one each player in turn.
        """
    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.type = ''
        self.score = 0

    def setType(self, s):
        self.type = s

    def giveType(self):
        return self.type

    def scorePoint(self):
        self.score += 1

    def __str__(self):
        return 'The {0} named {1} has scored {2} points'.format(self.type, self.name, str(self.score))


def getPlayers(l):
    print('This is a game for two players.\nOne of whom is the computer.')
    try:
        ui = input('What should the computer be called? ').strip().title()
        player1 = Player(ui)
        player1.setType('computer')
        l.append(player1)
        logging.debug('player1 created')
    except Exception as e:
        print(e)
        logging.debug('Exception capturing computer name: {0}'.format(e))

    print('OK, and now we need another player...')
    try:
        ui = input('What is your name? ').strip().title()
        player2 = Player(ui)
        player2.setType('human')
        l.append(player2)
        logging.debug('player2 created')
    except Exception as e:
        print(e)
        logging.debug('Exception capturing human name: {0}'.format(e))


def doRound(i, player):
    logging.debug('round {0}, player is {1}'.format(i, player.type))
    i = Round(player)
    i.start()
    i.play()
    if i.checkWin:
        player.scorePoint


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
    # playerNow.setTurn
    doRound(roundsPlayed, playerNow)
    print('Here are the scores after round {0}:'.format(roundsPlayed))
    getScores(l)
    # playerNow.unsetTurn
    q.append(playerNow) # player whose turn has just ended is now at q(1)

    while True:
        try:
            ui = input('Play again? ').strip().lower()
            if ui in ('y', 'yes'):
                # play more rounds
                roundsPlayed += 1
                playerNow = q.pop(0)
                # playerNow.setTurn
                doRound(roundsPlayed, playerNow)
                print('Here are the scores after round {0}:'.format(roundsPlayed))
                getScores(l)
                # playerNow.unsetTurn
                q.append(playerNow) # now at q(1)

            elif ui in ('n', 'no'):
                break
            else:
                print('Please enter yes or no.')
        except Exception as e:
            print(e)
            logging.debug('Exception capturing play again choice: {0}'.format(e))

    print('OK, the game is over. The final scores are: ')
    getScores(l)
    logging.debug('End of program')


if __name__ == '__main__':
    print('Welcome to Hangman!')
    main()
