# https://www.hackerrank.com/challenges/repeated-string/problem

def repeatedString(s, n):
    l = len(s)
    m = n % l
    d = n // l
    count = s.count('a') * d + s[:m].count('a')
    return count


if __name__ == '__main__':
    s = input()
    n = int(input())

    result = repeatedString(s, n)
    print(result)
