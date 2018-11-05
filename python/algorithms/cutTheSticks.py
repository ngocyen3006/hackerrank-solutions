# https://www.hackerrank.com/challenges/cut-the-sticks/problem


def cutTheSticks(arr):
    n = len(arr)
    count = {}
    for i in arr:
        count.setdefault(i, 0)
        count[i] += 1
    k = sorted(count.keys())
    res = [n]
    for i in k:
        n = n - count[i]
        if n > 0:
            res.append(n)
    return res


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)
    print(*result, sep='\n')
