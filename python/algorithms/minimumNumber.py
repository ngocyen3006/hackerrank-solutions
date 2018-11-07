# https://www.hackerrank.com/challenges/strong-password/problem

import re


def minimumNumber(n, password):
    '''
    Return the minimum number of characters to make the password strong
    '''
    count = 0
    res = 0
    if n < 6:
        res = 6 - n
    if not bool(re.search('[A-Z]', password)):
        count = count + 1
    if not bool(re.search('[0-9]', password)):
        count += 1
    if not bool(re.search('[a-z]', password)):
        count += 1
    if not bool(re.search('[!@#$%^&*()\-+]', password)):
        count += 1
    if count < res:
        return res
    return count


if __name__ == '__main__':
    n = int(input())
    password = input()

    answer = minimumNumber(n, password)
    print(answer)
