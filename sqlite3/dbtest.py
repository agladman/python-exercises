#!/usr/bin/env python3

"""
sandbox for learning how to use sqlite3 with python
"""

import sqlite3


con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS butts (butt_id INTEGER PRIMARY KEY AUTOINCREMENT, cheeks INTEGER, look TEXT, fart_power REAL NOT NULL)''')

# lotsa_butts = [(2, 'cheeky', 9.37),
#                 (2, 'pert', 4.29),
#                 (2, 'smelly', 9.99),
#                 (1, 'lopsided', 1.76),
#                 (2, 'normcore', 3.92),
#                 (2, 'smooth', 2.01),
#                 (2, 'rounded', 4.40),
#                 (2, 'wobbly', 5.23),
#                 (2, 'bubble', 7.91),
#                 (2, 'dick', 2.63)]
#
# cur.executemany('''INSERT INTO butts (cheeks, look, fart_power) VALUES (?, ?, ?)''', lotsa_butts)

def get_avg_fart_power() -> float:
    "calculates the average fart power of the butts recorded in the db"
    afp = cur.execute('''SELECT AVG(fart_power) FROM butts''')
    return afp.fetchone()[0]    # afp.fetchone() comes back as a tuple e.g. (5.151, )

def get_farty_butts(fp=None) -> list:
    "returns a list of butts with above-average fart power"
    if fp is None:
        fp = get_avg_fart_power()
    res = cur.execute(f'''SELECT *
                        FROM butts
                        WHERE fart_power >= {fp}
                        ORDER BY fart_power ASC''')
    return res.fetchall()  # returns a list of results rather than a cursor object

def get_butts(letter) -> list:
    "fetches all butts that contain a given letter in the look field"
    butts = cur.execute(f'''SELECT *
    FROM butts
    WHERE instr(look, '{letter}') > 0
    ORDER BY fart_power DESC''')
    return butts.fetchall()

def check_butts():
    req = input('Enter a letter: ')
    res = get_butts(req)
    if res:
        print(f'butts containing {req}:')
        for r in res:
            _, _, a, _ = r
            print(' ' + a)
    else:
        print(f'No butts found containing {req}')

def add_butt(lk, fp, ch=2):
    "adds a butt to the database"
    try:
        cur.execute('''INSERT INTO butts (cheeks, look, fart_power) VALUES (?, ?, ?)''', (ch, lk, fp))
        return True
    except Exception as e:
        raise e
        return False

def gather_new_butts():
    "prompts user for info on new butts to add to the database"
    while True:
        lk = input("Enter a butt to add to the database: ")
        fp = float(input("Enter its fart power: "))
        ch = input("Enter a number of buttcheeks, or leave blank for 2: ")
        ch = int(ch) if ch != '' else 2
        if add_butt(lk, fp, ch):
            cont = input("Do you want to add another? ")
            if cont in ('yes', 'Yes', 'y', 'Y'):
                continue
            else:
                break
    con.commit()

def show_above_avg_butts():
    "prints butts with above-average fart power"
    afp = get_avg_fart_power()
    print(f'butts with fart power of {afp:.2f} or higher:')
    butts = get_farty_butts()
    for b in butts:
        _, _, lk, fp = b
        print(f' {lk}\t- {fp:.2f}')

def main():
    gather_new_butts()
    show_above_avg_butts()
    check_butts()

if __name__ == '__main__':
    main()
    con.commit()
    con.close()
