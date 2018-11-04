# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

from math import sqrt, ceil, floor


# Method 1
def squares(a, b):
    a = ceil(sqrt(a))
    b = floor(sqrt(b))
    return int(b - a) + 1


# Method 2
def squares2(a, b):
    count = 0
    h = floor(sqrt(a))
    k = floor(sqrt(b))
    for i in range(h, k + 1):
        if i ** 2 in range(a, b + 1):
            count += 1
    return count


if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()
        a = int(ab[0])
        b = int(ab[1])

        result = squares(a, b)
        res = squares2(a, b)
        print(f"({result}, {res}) : {result==res}")
