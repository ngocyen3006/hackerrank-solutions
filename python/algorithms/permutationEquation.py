# https://www.hackerrank.com/challenges/permutation-equation/problem

def permutationEquation(p):
    n = len(p)
    y = [0] * n
    for x in range(1, n + 1):
        for i in range(n):
            if p[i] == x:
                temp = i + 1
        for j in range(n):
            if p[j] == temp:
                y[x - 1] = j + 1
    return y


if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)
    print(*result, sep='\n')
