#!/usr/bin/env python3
"""Like Knifey-Spooney, only more Boolean."""

def truthyfalsey(i, v):
    elist = "None True False '' [] ()".split()
    print(f'{i + 1}: x is {elist[i]}. If triggers: ', end='')
    iflist = []
    if v:
        # print('if x', end='')
        # iflist.append('if x')
        iflist.append('A')
    if not v:
        # print('if not x', end='')
        # iflist.append('if not x')
        iflist.append('B')
    if v == True:
        # print('if x == True', end='')
        # iflist.append('if x == True')
        iflist.append('C')
    if v == False:
        # print('if x == False', end='')
        # iflist.append('if x == False')
        iflist.append('D')
    if v is True:
        # print('if x is True', end='')
        # iflist.append('if x is True')
        iflist.append('E')
    if v is False:
        # print('if x is False', end='')
        # iflist.append('if x is False')
        iflist.append('F')
    if v is not False:
        # print('if x is not False', end='')
        # iflist.append('if x is not False')
        iflist.append('G')
    if v is not True:
        # print('if x is not True', end='')
        # iflist.append('if x is not True')
        iflist.append('H')
    ifstring = ', '.join([x for x in iflist])
    print(f'{ifstring}.', end = '')
    try:
        print(f' len(x): {len(v)}')
    except Exception as e:
        print(f' len(x): {e}')
        pass

empties = [None, True, False, '', [], ()]
print("""
If evaluation statements:
    A) if x,
    B) if not x,
    C) if x == True,
    D) if x == False,
    E) if x is True,
    F) if x is False,
    G) if x is not False,
    H) if x is not True
    """)
for i, v in enumerate(empties):
    truthyfalsey(i, v)
