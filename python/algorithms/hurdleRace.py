# https://www.hackerrank.com/challenges/the-hurdle-race/problem

def hurdleRace(k, height):
    maximum = max(height)
    return max(maximum - k, 0)


if __name__ == '__main__':
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    height = list(map(int, input().rstrip().split()))

    result = hurdleRace(k, height)
    print(result)
