# https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandles(ar):
    maxar = ar[0]
    count = {}
    for i in ar:
        count.setdefault(i, 0)
        count[i] += 1
        if i > maxar:
            maxar = i
    return count[maxar]


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)
    print(result)
