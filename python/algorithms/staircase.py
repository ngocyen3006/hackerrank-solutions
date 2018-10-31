# https://www.hackerrank.com/challenges/staircase/problem

def staircase(n):
    c = "#"
    for i in range(1, n + 1):
        print((c * i).rjust(n))


if __name__ == '__main__':
    n = int(input())

    staircase(n)
