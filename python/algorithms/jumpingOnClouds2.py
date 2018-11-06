# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

def jumpingOnClouds(c):
    i = 0
    count = 0
    while i < len(c) - 2:
        count += 1
        if c[i + 2] == 1:
            i += 1
            continue
        i += 2
    if i == n - 2:
        count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)
    print(result)
