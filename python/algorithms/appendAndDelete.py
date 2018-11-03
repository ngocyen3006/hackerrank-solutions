# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    if len(s) + len(t) <= k or s == t:
        return "Yes"
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            continue
        break
    if len(s[i:]) + len(t[i:]) != k:
        return "No"
    return "Yes"


if __name__ == '__main__':
    s = input()
    t = input()
    k = int(input())

    result = appendAndDelete(s, t, k)
    print(result)
