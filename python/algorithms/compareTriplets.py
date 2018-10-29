# https://www.hackerrank.com/challenges/compare-the-triplets/problem

def compareTriplets(a, b):
    result = [0, 0]
    for i in range(len(a)):
        if a[i] > b[i]:
            result[0] += 1
            continue
        if b[i] > a[i]:
            result[1] += 1
            continue
    return result


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(*result)
