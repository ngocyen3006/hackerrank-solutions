# https://www.hackerrank.com/challenges/2d-array/problem

def hourglassSum(arr):
    maximum = -63
    for i in range(1, 5):
        for j in range(1, 5):
            sum = arr[i][j] \
                  + arr[i - 1][j - 1] + arr[i - 1][j] + arr[i - 1][j + 1] \
                  + arr[i + 1][j - 1] + arr[i + 1][j] + arr[i + 1][j + 1]
            maximum = max(maximum, sum)
    return maximum


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print(result)
