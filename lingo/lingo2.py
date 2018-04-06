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


from random import choice


with open('words.txt', 'r') as f:
    words = f.read().split()


class Round():
    """Represents one iteraton of the lingo game."""

    def __init__(self, n=5):
        self.word_length = n
        self.secret_word = ''
        self.won = False
        self.set_secret_word()

    def clean_word(self, word):
        """Strips numbers and punctuation from a word."""
        output = filter(str.isalpha, word)
        return ''.join(output)

    def set_secret_word(self):
        """Generates the word the player must guess."""
        while True:
            candidate = self.clean_word(choice(words).lower())
            if len(candidate) == self.word_length:
                self.secret_word = candidate
                break

    def guess(self, word):
        """Compares a player's guess against the secret word."""
        if word == self.secret_word:
            self.won = True
            output = f'Correct, the word was indeed {word}.'
        else:
            chars = list(word)
            matches = {}
            for i, ch in enumerate(chars):
                if ch in self.secret_word:
                    matches[i] = ch
            for k, v in matches.items():
                if matches[k] == self.secret_word[k]:
                    chars[k] = f'[{v}]'
                else:
                    chars[k] = f'({v})'
            output = ''.join(chars)
        return output


class Player():
    """holds the player's name, score and number of rounds played"""

    def __init__(self, name):
        self.name = name
        self.score = 0
        self.rounds_played = 0

    def get_scores(self):
        print(f"""\n{self.name} has played {self.rounds_played} round{'' if self.rounds_played == 1 else 's'} and scored {self.score} point{'' if self.score == 1 else 's'}.""")


def show_rules():
    print("""
        The computer will choose a random word. By default the word is
        five letters long, but you can choose to make it shorter or
        longer, up to a maximum of 15 characters.

        You have to guess this word. Each time you guess, your chosen
        word will be returned with two types of clues included in it.

        1) If a letter in your guess is also in the secret word, but in
        a different position, it will be marked in parentheses.

        2) If a letter in your guess is also in the secret word, and in
        the same position, it will be marked in square brackets.

        For example, if the secret word is "tiger" and you guess "tulip"
        the clue you get back will be "[t]ul(i)p".
        """)


def get_word_length():
    print('How long should the word be?')
    while True:
        ui = input('\nEnter a number between 1 and 15 or leave blank for the default length (5). ')
        if ui == '':
            return 5
            break
        elif ui.isdecimal():
            ui = int(ui)
            if 0 < ui <= 15:
                return ui
                break


def play_round(roundnum, player):
    n = get_word_length()
    roundnum = Round(n)
    while not roundnum.won:
        ui = input('\nGuess a word or type quit to give up: ').strip().lower()
        if ui == 'quit':
            player.rounds_played += 1
            print(f'OK, round over. The word was "{roundnum.secret_word}".')
            break
        elif ui.isalpha():
            if len(ui) == roundnum.word_length:
                clue = roundnum.guess(ui)
                print(f'Clue: {clue}')
            elif len(ui) < roundnum.word_length:
                print('That guess was too short, '
                      f'try again with a {str(roundnum.word_length)}-letter word.')
            elif len(ui) > roundnum.word_length:
                print('That guess was too long, '
                      f'try again with a {str(roundnum.word_length)}-letter word.')
            else:
                print('I don\'t know what went wrong, but something did.')
                pass
        else:
            print(f'Invalid guess. Please try a {str(roundnum.word_length)}-letter word.')
    if roundnum.won:
        player.rounds_played += 1
        player.score += 1


def main():
    print('\n\nWelcome to Lingo!\n\n')

    while True:
        ui = input('Would you like to read the rules? ').strip().lower()
        if ui in ('y', 'yes'):
            show_rules()
            break
        elif ui in ('n', 'no'):
            break
        else:
            print('Please enter yes or no.')

    while True:
        ui = input('What\'s your name? ').strip().title()
        if ui:
            player = Player(ui)
            break
        else:
            print('Go on, tell me your name.')

    i = 1
    play_round(i, player)
    player.get_scores()

    while True:
        ui = input('\nPlay again? ').strip().lower()
        if ui in ('y', 'yes'):
            i += 1
            play_round(i, player)
            player.get_scores()
        elif ui in ('n', 'no'):
            print('\nThanks for playing Lingo!\n\n')
            break
        else:
            print('Please enter yes or no.')


if __name__ == '__main__':
    main()
