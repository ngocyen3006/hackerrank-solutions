# https://www.hackerrank.com/challenges/maximum-draws/problem


def maximumDraws(n):
    return n + 1


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = maximumDraws(n)
        print(result)
