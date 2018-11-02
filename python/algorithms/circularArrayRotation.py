# https://www.hackerrank.com/challenges/circular-array-rotation/problem

def circularArrayRotation(a, k, queries):
    res = []
    for i in queries:
        res.append(a[i - k % len(a)])
    return res


if __name__ == '__main__':
    nkq = input().split()
    n = int(nkq[0])
    k = int(nkq[1])
    q = int(nkq[2])
    a = list(map(int, input().rstrip().split()))

    queries = []
    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print(*result, sep='\n')
