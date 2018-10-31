# https://www.hackerrank.com/challenges/sock-merchant/problem

def sockMerchant(n, ar):
    count = {}
    for i in ar:
        count.setdefault(i, 0)
        count[i] += 1

    result = 0
    for k in count.keys():
        result += (count[k] // 2)

    return result


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)
    print(result)
