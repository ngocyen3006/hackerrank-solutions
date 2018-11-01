# https://www.hackerrank.com/challenges/counting-valleys/problem


def countingValleys(n, s):
    step = 0
    valleys = 0
    for i in range(n):
        if s[i] == "U":
            step += 1
        else:
            step -= 1

        if step == 0 and s[i] == "U":
            valleys += 1
    return valleys


if __name__ == '__main__':
    n = int(input())
    s = input()

    result = countingValleys(n, s)
    print(result)
