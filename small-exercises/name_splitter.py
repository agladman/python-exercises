#!/usr/bin/env python3

def generate_email():
    """generates email address for a given full name
    expects at least a first and last name so wouldn't work for Cher or Madonna
    """
    ui = input('Enter full name: ')
    first, *middle, last = ui.lower().split()
    if middle:
        initials = ''.join(m[0] for m in middle)
        email_string = f'{first}.{initials}.{last}@gmail.com'
    else:
        email_string = f'{first}.{last}@gmail.com'
    return email_string

if __name__ == '__main__':
    e = generate_email()
    print(f'Your email is {e}')
