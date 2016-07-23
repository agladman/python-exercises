#!/usr/bin/env Python3

secret_word = 'beefy'

testwords = ['boney', 'beery', 'freed']

def guess(word):
        chars = list(word)
        matches = {}
        for i, ch in enumerate(chars):
            if ch in secret_word:
                matches[i] = ch
        for k, v in matches.items():
            if matches[k] == secret_word[k]:
                chars[k] = '[{0}]'.format(v) 
            else:
                chars[k] = '({0})'.format(v)
        return ''.join(chars)

print(' word: {0}'.format(secret_word))
for word in testwords:
    print('guess: {0}; result: {1}.'.format(word, guess(word)))
