# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    max = scores[0]
    min = scores[0]
    count = [0, 0]
    for i in scores:
        if i < min:
            count[1] += 1
            min = i
            continue
        if i > max:
            count[0] += 1
            max = i
            continue
    return count


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(*result)
