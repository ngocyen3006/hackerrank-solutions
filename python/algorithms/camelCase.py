# https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    count = [i for i in s if i.isupper()]
    return len(count) + 1


if __name__ == '__main__':
    s = input()

    result = camelcase(s)
    print(result)
