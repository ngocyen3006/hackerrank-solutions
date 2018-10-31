# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    count = {}
    for i in arr:
        count.setdefault(i, 0)
        count[i] += 1

    common = []
    value = max(count.values())
    for k, v in count.items():
        if count[k] == value:
            common.append(k)
    return min(common)


if __name__ == '__main__':
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)
    print(result)
