# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

def jumpingOnClouds(c, k):
    e = 100
    for i in range(0, n, k):
        if c[i] == 0:
            e = e - 1
            continue
        e = e - 3
    return e


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)
    print(result)
