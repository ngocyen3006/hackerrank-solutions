# https://www.hackerrank.com/challenges/array-left-rotation/problem
def leftRotation(arr, d):
    return arr[d:] + arr[:d]


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])
    a = list(map(int, input().rstrip().split()))

    res = leftRotation(a, d)
    print(*res)
