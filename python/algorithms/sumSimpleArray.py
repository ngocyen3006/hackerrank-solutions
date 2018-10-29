# https://www.hackerrank.com/challenges/simple-array-sum/problem

# !/bin/python3


# Complete the simpleArraySum function below.

def simpleArraySum(ar):
    n = len(ar)
    sum = 0
    for i in range(n):
        sum += ar[i]
    return sum


if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)
