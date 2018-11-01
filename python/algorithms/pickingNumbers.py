# https://www.hackerrank.com/challenges/picking-numbers/problem

# Method 1
def pickingNumbers(a):
    res = []
    for i in range(len(a)):
        temp = [a[i]]
        for j in range(len(a)):
            if j != i and (a[i] - a[j] == 1 or a[i] == a[j]):
                temp.append(a[j])
        res.append(temp)
    maximum = 0
    for i in res:
        if len(i) > maximum:
            maximum = len(i)
    return maximum


# Method 2
def pickingNumbers2(a):
    maximum = 0

    for i in a:
        num = a.count(i) + a.count(i - 1)
        maximum = max(maximum, num)

    return maximum


if __name__ == '__main__':
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    result1 = pickingNumbers(a)
    print(result1)

    result2 = pickingNumbers2(a)
    print(result2)
