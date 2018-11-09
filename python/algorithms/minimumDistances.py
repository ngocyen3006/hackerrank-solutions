# https://www.hackerrank.com/challenges/minimum-distances/problem

def minimumDistances(a):
    minimum = len(a) + 1
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[j] == a[i]:
                minimum = min(minimum, j - i)

    if minimum == len(a) + 1:
        return -1
    return minimum


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)
    print(result)
