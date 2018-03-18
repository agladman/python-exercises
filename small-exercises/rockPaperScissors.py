#!/usr/bin/env python3

"""You must make a rock paper scissors game
Goal
Ask the player if they pick rock paper or scissors
Have the computer chose its move
Compare the choices and decide who wins
Print the results
Subgoals
Let the player play again
Keep a record of the score e.g. (Player: 3 / Computer: 6)"""

from random import randint, choice

choices = { '1': 'rock', '2': 'paper', '3': 'scissors'}
insults = ['cunt', 'motherfucker', 'wanker', 'piss stain', 'shit for brains', 'moron', 'fucker', 'little shit', 'loser', 'prick', 'numpty', 'jizz stain']
exclamations = ['shit', 'fuck', 'piss', 'balls', 'arse', 'bugger', 'cunt', 'piss on my brains', 'fuck it', 'wank me sideways with a shovel']
adjecfuckingtives = ['fucking', 'shitting', 'pissing', 'sodding', 'pigging', 'motherfucking', 'bloody']

def swear(listname):
        return choice(listname)

def compChoose():
    n = randint(1,3)
    return choices[str(n)]

def playerChoose():
    while True:
        try:
            n = input('Choose rock (1), paper (2) or scissors (3): ')
        except ValueError:
            print('I don\'t know what you did to fuck this up but don\'t {} do it again you {}'.format(swear(adjecfuckingtives), swear(insults)))
            continue

        if n not in ('1', '2', '3'):
            print('Invalid {} choice, you {}. Enter 1, 2 or 3 only.'.format(swear(adjecfuckingtives), swear(insults)))
            continue

        else:
            return choices[n]
            break

    # while True:
    #     n = input('Choose rock (1), paper (2) or scissors (3): ')
    #     if n in choices.keys():
    #         return choices[n]
    #         break
    #     else:
    #         print('\nInvalid {} choice, you {}. Enter 1, 2 or 3 only.'.format(swear(adjecfuckingtives), swear(insults)))

def pickWinner(l):
    if l[0] == l[1]:
        return False
    elif 'scissors' not in l:
        return 'paper'
    elif 'paper' not in l:
        return 'rock'
    else:
        return 'scissors'

def playRound():
    haveWinner = False
    while haveWinner == False:
        a = playerChoose()
        b = compChoose()
        print('\nYou chose {}, I chose {} {}. '.format(a, swear(adjecfuckingtives), b), end = '')
        round = [a, b]
        c = pickWinner(round)
        if c == a:
            print('{}! You won!'.format(swear(exclamations).capitalize()))
            winner = 'Puny Human'
            haveWinner = True
        elif c == b:
            print('Haha! I won! Suck it, {}!'.format(swear(insults)))
            winner = 'Computer'
            haveWinner = True
        else:
            print('No {} fucker won. Choose again, {}.'.format(swear(adjecfuckingtives), swear(insults)))

    return winner

def giveScores(roundsPlayed, scores, isFinal=None):
    finaliser = ''
    finaliser = 'final ' if isFinal else finaliser

    pluraliser = 's'
    pluraliser = '' if roundsPlayed == 1 else pluraliser

    print('\nAfter {} round{} the {}scores are: Puny {} Human {} / Computer {}'.format(roundsPlayed, pluraliser, finaliser, swear(adjecfuckingtives).title(), scores['Puny Human'], scores['Computer']))


def main():
    print('\nWelcome, Puny Human! Let us play...\n\nTHE ROCK, THE PAPER AND THE {} SCISS{}RS!'.format(swear(adjecfuckingtives).upper(), 'O' * randint(4,10)))

    # 1st round
    scores = {'Puny Human': 0, 'Computer': 0}
    roundsPlayed = 0
    scores[playRound()] += 1
    roundsPlayed += 1

    giveScores(roundsPlayed, scores)

    # 2nd and subsequent rounds
    while True:
        print('Play again? Enter yes or no: ', end = '')
        yesNo = input().lower()
        if yesNo.startswith('y'):
            scores[playRound()] += 1
            roundsPlayed += 1
            giveScores(roundsPlayed, scores)

        elif yesNo.startswith('n'):
            isFinal = True
            giveScores(roundsPlayed, scores, isFinal)
            if scores['Puny Human'] > scores['Computer']:
                print('\n{}! You {} beat me! YOU {} {}! {}!'.format(swear(exclamations).capitalize(), swear(adjecfuckingtives), swear(adjecfuckingtives).upper(), swear(insults).upper(), swear(exclamations).upper()))
            elif scores['Puny Human'] == scores['Computer']:
                print('\nFuck me, it\'s a draw. How {} dull.'.format(swear(adjecfuckingtives)))
            else:
                print('\nAAAAAAAH! I {} BEAT YOU, YOU {}! YEAH!'.format(swear(adjecfuckingtives).upper(), swear(insults).upper()))
                print('\nYEAH!')
                print('\n\nYEEEEEEEEEEEEEEAAAAAHHH!')
            break
        else:
            print('\n{}, can\'t you even get a simple yes/no question right?'.format(swear(insults).capitalize()))

main()
