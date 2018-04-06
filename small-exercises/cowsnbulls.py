#!/usr/bin/env python3

"""
Create a program that will play the “cows and bulls” game with the user.
The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have
a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.

Keep track of the number of guesses the user makes throughout the game and tell
the user at the end.
"""


from random import randint, shuffle


class GameRound():
    """One round of the cows and bulls game."""
    _number = ''
    _hint = ['_'] * 4
    _hint_nums = [0, 1, 2, 3]
    _guesses = 0
    _won = False
    _limit = None

    def __init__(self, limit=None):
        """Sets the secret number and the guess limit (if specified)."""
        self._number = ''.join(str(n) for n in self.set_number())
        self._limit = limit

    def __repr__(self):
        """Returns a string formatted for repr()."""
        s = '<{0}.{1}; _number {2}; _guesses {3}; _limit {4}; _won {5}>'.format(
            self.__module__,
            type(self).__name__,
            self._number,
            self._guesses,
            self._limit,
            self._won)
        return s

    def __str__(self):
        """Returns a string displaying the current state of play."""
        if self._won:
            x = 'won'
        else:
            x = 'not won'
        s = check_plural('guess', self._number)
        return f'In this round the number is {self._number}. After {self._guesses} {s} the round is {x}.'

    def set_number(self):
        """Yields a random four-digit number."""
        for _ in range(4):
            yield randint(0, 9)

    def play(self):
        """Collects guesses until a) user wins, b) user runs out of guesses, or c) user quits."""
        while self._won == False:
            if not self._limit:
                ui = self.get_input()
                if ui == 'q':
                    print('User quit.')
                    print(self)
                    break
                else:
                    self.guess(ui)
            else:
                if self._guesses < self._limit:
                    ui = self.get_input()
                    if ui == 'q':
                        print('User quit.')
                        print(self)
                        break
                    else:
                        self.guess(ui)
                else:
                    print('Ran out of guesses.')
                    print(self)
                    break

    def get_input(self):
        """Collects and validates user input."""
        while True:
            ui = input('Enter a number or "q" to quit: ')
            if ui == 'q':
                break
            elif ui == 'h':     # secret option not mentioned to user
                self.show_hint()
            elif len(ui) != 4:
                print('Your guess must be four digits long, try again.')
            elif not self.alpha_check(ui):
                break
            else:
                print('You guess cannot contain letters. Try again.')
        return ui

    @staticmethod
    def alpha_check(somestring):
        """Returns True if any letters are present in a string."""
        for ch in somestring:
            if ch.isalpha():
                return True

    def guess(self, number):
        """Runs the guess through the compare() function and prints the result."""
        cows, bulls = self.compare(number)
        print(f'{cows} {check_plural("cow", cows)}, {bulls} {check_plural("bull", bulls)}.')
        self._guesses += 1
        if cows == 4:
            print('\nCorrect!')
            self._won = True
            print(self)

    def compare(self, num_string):
        """Compares the guess with the hidden number."""
        cows = 0    # right number, right place
        bulls = 0   # right number, wrong place
        for idx, ch in enumerate(num_string):
            if ch == self._number[idx]:
                cows += 1
            elif ch in self._number:
                bulls += 1
        return cows, bulls

    def show_hint(self):
        """Reveals the number one digit at a time. Currently unlimited so will
            eventually reveal the whole number."""
        if len(self._hint_nums) > 0:
            shuffle(self._hint_nums)
            n = self._hint_nums.pop(0)
            self._hint[n] = self._number[n]
            print(''.join(ch for ch in self._hint))
        else:
            print(self._hint)


def check_plural(word, number):
    """Pluralises words if required."""
    if number != 1:
        if word.endswith('s'):
            word = word + 'es'
        else:
            word = word + 's'
    return word


def show_rules():
    """Displays game rules to the user."""
    print("""

The computer is thinking of a four-digit number. You must try to guess this number.

Each time you guess the computer will give you clues to how close you are.
For each digit you guess correctly in the correct position, you get a 'cow'.
For each digit you guess correctly but in the wrong place, you get a 'bull'.

For example, if the number is 8025, and you guess 8539, you will get:

    >>> 1 cow, 1 bull.

If you guess 5890 next, you will get:

    >>> 0 cows, 3 bulls.

You must get 4 cows to win each round.

""")


def ask(activity):
    affirmations = 'y yes yup ok sure'.split()  # better using a set somehow?
    reply = input(f'Would you like to {activity}? ')
    if reply.lower() in affirmations:
        return True
    else:
        return False


def main():
    print('\nWelcome to Cows and Bulls.')
    if ask('read the rules'):
        show_rules()
    limit = int(input('\nEnter the number of guesses in each round or hit enter for unlimited guesses: '))
    print('\nOK let\'s play!')
    while True:
        g = GameRound(limit)
        g.play()
        if not ask('play again'):
            break
    print('\nThanks for playing!')


if __name__ == '__main__':
    main()
