# https://www.hackerrank.com/challenges/arrays-ds/problem


def reverseArray(a):
    return list(reversed(a))


if __name__ == '__main__':
    arr_count = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)
    print(*res)
