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
insults = ['cunt', 'motherfucker', 'wanker', 'piss stain', 'shit for brains', 'cum dumpster', 'moron', 'fucker', 'little shit', 'loser']
exclamations = ['Shit!', 'Fuck!', 'Piss!', 'Balls!', 'Arse!']
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
            return choices[n] if n in choices
            break
        except ValueError:
            print('Generic error message')
        except IndexError:
            print('Generic error message')

    # while True:
    #     n = input('Choose rock (1), paper (2) or scissors (3): ')
    #     if n in choices.keys():
    #         return choices[n]
    #         break
    #     else:
    #         print('\nInvalid %s choice, you %s. Enter 1, 2 or 3 only.' % (choice(adjecfuckingtives), choice(insults)))

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
        print('\nYou chose %s, I chose %s %s. ' % (a, choice(adjecfuckingtives), b), end = '')
        round = [a, b]
        c = pickWinner(round)
        if c == a:
            print('%s You won!' % (choice(exclamations)))
            winner = 'Puny Human'
            haveWinner = True
        elif c == b:
            print('Haha! I won! Suck it, %s!' % (choice(insults)))
            winner = 'Computer'
            haveWinner = True
        else:
            print('No %s fucker won.' % (choice(adjecfuckingtives)))

    return winner

def main():
    print('\nWelcome, Puny Human! Let us play...\n\nTHE ROCK, THE PAPER AND THE %s SCISSOOOOORS!' % (choice(adjecfuckingtives).upper()))

    # 1st round
    scores = {'Puny Human': 0, 'Computer': 0}
    roundsPlayed = 0
    scores[playRound()] += 1
    roundsPlayed += 1

    print('\nAfter %i round the scores are: Puny %s Human %i / Computer %i' % (roundsPlayed, choice(adjecfuckingtives).capitalize(), scores['Puny Human'], scores['Computer']))

    # 2nd and subsequent rounds
    while True:
        print('Play again? Enter yes or no: ', end = '')
        yesNo = input().lower()
        if yesNo.startswith('y'):
            scores[playRound()] += 1
            roundsPlayed += 1
            print('\nAfter %i rounds the scores are: Puny %s Human %i / Computer %i' % (roundsPlayed, choice(adjecfuckingtives).capitalize(), scores['Puny Human'], scores['Computer']))

        elif yesNo.startswith('n'):
            print('\nAfter %i rounds the final %s scores are: Puny %s Human %i / Computer %i' % (roundsPlayed, choice(adjecfuckingtives), choice(adjecfuckingtives).capitalize(), scores['Puny Human'], scores['Computer']))
            if scores['Puny Human'] > scores['Computer']:
                print('\n%s You %s beat me! YOU %s %s! %s' % (choice(exclamations).capitalize(), choice(adjecfuckingtives), choice(adjecfuckingtives).upper(), choice(insults).upper(), choice(exclamations).upper()))
            elif scores['Puny Human'] == scores['Computer']:
                print('\nFuck me, it\'s a draw. How %s dull.' % (choice(adjecfuckingtives)))
            else:
                print('\nAAAAAAAH! I %s BEAT YOU, YOU %s! YEAH!' % (choice(adjecfuckingtives).upper(), choice(insults).upper()))
                print('\nYEAH!')
                print('\n\nYEEEEEEEEEEEEEEAAAAAHHH!')
            break
        else:
            print('\n%s, can\'t you even get a simple yes/no question right?' % (choice(insults).capitalize()))

main()
