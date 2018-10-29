# https://www.hackerrank.com/challenges/diagonal-difference/problem

import math


def diagonalDifference(arr):
    n = len(arr) - 1
    d1 = 0
    d2 = 0
    for i in range(n + 1):
        d1 += arr[i][i]
        d2 += arr[i][n - i]
    return abs(d1 - d2)


if __name__ == '__main__':
    n = int(input())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
