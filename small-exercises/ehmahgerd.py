#!/usr/bin/env python3


"""Some stupid bullshit, basically because I thought
    I could code a better version of this: https://pastebin.com/3Fh0YUY1
    """


import re


class Word:

    def __init__(self, my_text):
        self._text = my_text
        self._vowels = set('aeiou')
        self.initial_th_to_d()
        self.concatenate_multiple_vowels()
        self.vowels_to_er()
        self.final_y_to_ah()

    def __len__(self):
        return len(self._text)

    def __repr__(self):
        return self._text

    def initial_th_to_d(self):
        """Makes words like 'this' like 'dis'."""
        if self._text.startswith('th'):
            self._text = ''.join('d' + self._text[2:])

    def final_y_to_ah(self):
        """Makes words like 'my' like 'mah'.
            Words ending in that initially ended in 'ey' before passing through _vowels_to_er() become 'err'.
            Example: 'they' becomes 'therr', or actually 'derr' - see aslo initial_th_to_d().
            """
        if self._text.endswith('ery'):
            self._text = ''.join(self._text[:-1] + 'r')
        if len(self) >= 2 and self._text[-1] == 'y' and self._text[-2] not in self._vowels:
            self._text = ''.join(self._text[:-1] + 'ah')

    def concatenate_multiple_vowels(self):
        """Where two or more vowels are grouped together, remove all but the last vowels."""

        def my_inner_func(self):
            vowels = set('aeiou')
            words = self._text.split()
            for word in words:
                letters = []
                for ch in word:
                    if len(letters) == 0:
                        letters.append(ch)
                    else:
                        if ch not in vowels:
                            letters.append(ch)
                        if ch in vowels and letters[-1] not in vowels:
                            letters.append(ch)
                        else:
                            pass
                for l in letters:
                    yield l
                yield ' '
        
        self._text = ''.join(my_inner_func(self)).rstrip(' ')


    def vowels_to_er(self):
        """Changes vowels to 'er' but skips 'e' at the end of words."""
        if self._text[-1] == 'e':
            self._text = re.sub(r'[aeiou]', 'er', self._text[:-1]) + 'e'
        else:
            self._text = re.sub(r'[aeiou]', 'er', self._text)



def convert_to_stupid(my_text):
    """Converts a string to idiotspeak."""
    words = my_text.split()
    result = [Word(w) for w in words]
    return ' '.join(str(r) for r in result)


def test():
    print(convert_to_stupid(input('Enter text: ')))


# def vowels(my_string):
#     vowels = set('aeiou')
#     for idx, ch in enumerate(my_string):
#         if ch not in vowels:
#             yield ch
#         else:
#             if my_string[idx - 1] in vowels:
#                 pass
#             else:
#                 yield c


# def vowels2(my_string):
#     vowels = set('aeiou')
#     words = my_string.split()
#     for word in words:
#         letters = []
#         for ch in word:
#             if len(letters) == 0:
#                 letters.append(ch)
#             else:
#                 if ch not in vowels:
#                     letters.append(ch)
#                 if ch in vowels and letters[-1] not in vowels:
#                     letters.append(ch)
#                 else:
#                     pass
#         for l in letters:
#             yield l

#         yield ' '


# def vv():
#     return ''.join(vowels2(input('text: '))).rstrip(' ')


if __name__ == '__main__':
    test()
