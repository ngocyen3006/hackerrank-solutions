# https://www.hackerrank.com/challenges/save-the-prisoner/problem


def saveThePrisoner(n, m, s):
    if (m + s - 1) % n == 0:
        return n
    return (m + s - 1) % n
