#!/usr/bin/env python3
"""Like Knifey-Spooney, only more Boolean."""


class DummyClass(object):
    pass


def truthyfalsey(i, v):
    """Evaluates empty variable v against different comparisons to True and False."""
    elist = "None True False '' [] () 0 0.0 foo bar baz DummyClass()".split()
    print(f'{i + 1}: x is {elist[i]}; if triggers: ', end='')
    iflist = []
    if v:
        iflist.append('A')
    if not v:
        iflist.append('B')
    if v == True:
        iflist.append('C')
    if v == False:
        iflist.append('D')
    if v is True:
        iflist.append('E')
    if v is False:
        iflist.append('F')
    if v is not False:
        iflist.append('G')
    if v is not True:
        iflist.append('H')
    ifstring = ', '.join([x for x in iflist])
    print(f'{ifstring}; ', end = '')
    try:
        print(f'bool(x): {bool(v)}; ', end='')
    except Exception as e:
        print(f'bool(x): {e}; ', end='')
        pass
    try:
        print(f'len(x): {len(v)}')
    except Exception as e:
        print(f'len(x): {e}')
        pass

foo, bar, baz, qux = ('eggs', True, False, DummyClass())
myvars = [None, True, False, '', [], (), 0, 0.0, foo, bar, baz, qux]
print(f"Empty vars tested: None, True, False, '', [], (), 0, 0.0")
print(f'Non-empty vars tested: foo = {foo}, bar = {bar}, baz = {baz}')
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
for i, v in enumerate(myvars):
    truthyfalsey(i, v)
