# https://www.hackerrank.com/challenges/big-sorting/problem


def bigSorting(unsorted):
    res = sorted(unsorted, key=int)
    return res


if __name__ == '__main__':
    n = int(input())

    unsorted = []
    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)
    print(*result, sep='\n')
