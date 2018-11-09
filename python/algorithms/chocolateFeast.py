# https://www.hackerrank.com/challenges/chocolate-feast/problem

# Method 1
def chocolateFeast(n, c, m):
    sum = n // c
    wrapper = sum
    while (wrapper // m) > 0:
        sum += wrapper // m
        wrapper = (wrapper // m) + (wrapper % m)
    return sum


# Method 2
def chocolateFeast2(n, c, m):
    return n // c + (n // c - 1) // (m - 1)


if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        ncm = input().split()
        n = int(ncm[0])
        c = int(ncm[1])
        m = int(ncm[2])

        result = chocolateFeast(n, c, m)
        res = chocolateFeast2(n, c, m)
        print(result, res)
