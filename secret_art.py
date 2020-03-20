"""
Passwords and secrets tools
"""

import string
import secrets


def password_generator(password_type=None, length=None) :
    """A random password generator
    
    password_type(str): the type of password, deciding charset
    length(int): password length, default 20 chars
    return(str): a random password
    raise: ValueError if wrong type
    """
    if length is None :
        password_length = 20
    elif length < 0 :
        raise ValueError('Length cannot be negative!')
    else :
        password_length = int(length)
    
    if password_type is None :
        password_type = 'plaintext'
    
    # Available charset
    _charset = {
        'mysql': string.ascii_letters + string.digits + r'!@#$%^&*',
        'ssh': string.ascii_letters + string.digits + r'~!@#$%^&*)(}{?+/=][,.><;:`',
        'username': string.ascii_letters + string.digits + '_',
        'plaintext': string.ascii_letters + string.digits
    }

    # Define charset according to password type
    try :
        alphabet = _charset[password_type]
    except KeyError :
        raise ValueError('Wrong type!')
    
    # A password consists of random characters
    password = ''.join(secrets.choice(alphabet) for i in range(password_length))
    # A username starts with a letter
    if password_type == 'username' :
        password = secrets.choice(string.ascii_letters) + password[1:]
    return password


def main() :
    # Parse arguments when executed in terminal
    from argparse import ArgumentParser
    from sys import exit
    parser = ArgumentParser(description='A password generator')
    parser.add_argument('--length', '-l', type=int, default=None, help='length, default to 20')
    parser.add_argument('--type', '-t', type=str, default=None,
        help='password types, including: mysql / ssh / username / plaintext(default)')
    args = parser.parse_args()
    
    try :
        password_to_show = password_generator(password_type=args.type, length=args.length)
    except ValueError as e :
        print('Something went wrong:', e)
        exit(2)
    print(password_to_show, end='')


if __name__ == '__main__' :
    main()
