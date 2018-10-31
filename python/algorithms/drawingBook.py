# https://www.hackerrank.com/challenges/drawing-book/problem

def pageCount(n, p):
    res1 = p // 2

    if n % 2 == 0:
        res2 = (n - p + 1) // 2
    else:
        res2 = (n - p) // 2

    if res1 < res2:
        return res1

    return res2


if __name__ == '__main__':
    n = int(input())
    p = int(input())

    result = pageCount(n, p)
    print(result)
