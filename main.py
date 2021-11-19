import requests
import hashlib
import sys

def hashing(lst):
    hashed = hashlib.sha1(lst.encode('utf-8')).hexdigest().upper()
    head, tail = (hashed[:5], hashed[5:])
    return head, tail

def get_hashes():
    head, tail = hashing(pas)
    url = f'https://api.pwnedpasswords.com/range/{head}'
    response = requests.get(url).text
    lsts = [line.split(':') for line in response.splitlines()]
    return lsts, tail

def check_pwned():
    lsts, tail = get_hashes()
    for lst in lsts:
        if lst[0] == tail:
            return f'There is a match, this password have been pwned {lst[1]} times'


passwords = sys.argv[1:]
if passwords == []:
    passwords = input('Please enter your passwords separated by spaces:   ')
    passwords = passwords.split()
for pas in passwords:
    if check_pwned() == None:
        print('Congratulations this password have not been pwned, go on ')
    else:
        print(check_pwned())





