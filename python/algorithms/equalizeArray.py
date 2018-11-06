# https://www.hackerrank.com/challenges/equality-in-a-array/problem

def equalizeArray(arr):
    count = {}
    for i in arr:
        count.setdefault(i, 0)
        count[i] += 1
    return len(arr) - max(count.values())


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)
