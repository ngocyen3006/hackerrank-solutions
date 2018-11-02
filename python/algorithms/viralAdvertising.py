# https://www.hackerrank.com/challenges/strange-advertising/problem

from math import floor


def viralAdvertising(n):
    liked = floor(5 / 2)
    cum = liked
    for i in range(2, n + 1):
        liked = floor(liked * 3 / 2)
        cum += liked
    return cum


if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)
    print(result)
