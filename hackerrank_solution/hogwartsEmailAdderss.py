#!/bin/python3

import string

def isValid(email):
    for i in range(5):
        if email[i] not in string.ascii_lowercase:
            return 'No'
    else:
        if email[5:] != '@hogwarts.com':
            return 'No'

    return 'Yes'

if __name__ == "__main__":
    s = input().strip()
    result = isValid(s)
    print(result)
