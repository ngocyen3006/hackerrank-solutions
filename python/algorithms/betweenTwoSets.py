# https://www.hackerrank.com/challenges/between-two-sets/problem

def getTotalX(a, b):
    factors = []
    x = 1
    while (max(a) * x) <= min(b):
        if max(a) * x %
        factors.append(max(a) * x)
        x += 1


    for i in factors:


    return len(result)


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)
    print(total)

