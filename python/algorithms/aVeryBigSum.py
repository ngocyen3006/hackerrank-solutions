# https://www.hackerrank.com/challenges/a-very-big-sum/problem

from functools import reduce


def aVeryBigSum(ar):
    return reduce(lambda x, y: x + y, ar, 0)


if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)
    print(result)
