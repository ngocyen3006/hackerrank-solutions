# https://www.hackerrank.com/challenges/beautiful-triplets/problem

# Method 1
def beautifulTriplets1(d, arr):
    count = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] - arr[i] == d:
                for k in range(j, len(arr)):
                    if arr[k] - arr[j] == d:
                        count += 1
    return count


# Method 2
def beautifulTriplets2(d, arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] + d in arr and arr[i] + 2 * d in arr:
            count += 1
    return count


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result1 = beautifulTriplets1(d, arr)
    result2 = beautifulTriplets2(d, arr)
    print((result1, result2))
