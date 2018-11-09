# https://www.hackerrank.com/challenges/service-lane/problem

def serviceLane(width, cases):
    return min(width[cases[0]:cases[1]+1])


if __name__ == '__main__':
    nt = input().split()
    n = int(nt[0])
    t = int(nt[1])
    width = list(map(int, input().rstrip().split()))

    for _ in range(t):
        cases = (list(map(int, input().rstrip().split())))

        result = serviceLane(width, cases)
        print(result)