# https://www.hackerrank.com/challenges/between-two-sets/problem

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) / gcd(a, b)


def gcdArray(arr):
    res = arr[0]
    for i in arr:
        res = gcd(res, i)

    return res


def lcmArray(arr):
    res = arr[0]
    for i in arr:
        res = lcm(res, i)

    return res


def getTotalX(a, b):
    lcmA = lcmArray(a)
    gcdB = gcdArray(b)

    count = 0
    x = 1
    while (lcmA * x) <= gcdB:
        if gcdB % (lcmA * x) == 0:
            count += 1
        x += 1

    return count


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)
    print(total)
