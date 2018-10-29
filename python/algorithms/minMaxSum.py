# https://www.hackerrank.com/challenges/mini-max-sum/problem

from functools import reduce


def miniMaxSum(arr):  # len(arr) = 5
    maxa = arr[0]
    mina = arr[0]
    sum = 0
    for i in arr:
        sum += i
        if i > maxa:
            maxa = i
        if i < mina:
            mina = i
    print(f"{sum - maxa} {sum - mina}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
