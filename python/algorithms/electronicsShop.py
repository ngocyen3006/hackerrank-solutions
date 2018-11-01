# https://www.hackerrank.com/challenges/electronics-shop/problem

from itertools import product


def getMoneySpent(keyboards, drives, b):
    max = - 1
    for k, d in product(keyboards, drives):
        if k + d > max and k + d <= b:
            max = k + d
    return max


