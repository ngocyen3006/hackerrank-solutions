# https://www.hackerrank.com/challenges/plus-minus/problem

def plusMinus(arr):
    n = len(arr)
    count = [0, 0, 0]
    for i in arr:
        if i > 0:
            count[0] += 1
            continue
        if i < 0:
            count[1] += 1
            continue

        count[2] += 1
    for i in count:
        print(round(i / n, 6))


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
