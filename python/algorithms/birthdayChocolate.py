# https://www.hackerrank.com/challenges/the-birthday-bar/problem


def birthday(s, d, m):
    count = 0
    for i in range(0, len(s) - m + 1):
        if sum(s[i:m]) == d:
            count += 1
        m += 1
    return count


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)
    print(result)
