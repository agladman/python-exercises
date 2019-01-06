#!/usr/bin/env python3


"""Changes all the vowels in a given string to upper case - but only the vowels."""


def vup_loop(mystring):
    result = ''
    for ch in mystring:
        if ch.lower() in 'aeiou':
            result += ch.upper()
        else:
            result += ch
    return result


def vup_generator(mychar):
    if mychar.lower() in 'aeiou':
        yield mychar.upper()
    else:
        yield mychar


def main():
    mystring = input('Enter a string: ')
    print(f'vup_loop():\t\t{vup_loop(mystring)}')

    s = ''.join(next(vup_generator(c)) for c in mystring)

    print(f'vup_generator():\t{s}')


if __name__ == '__main__':
    main()
