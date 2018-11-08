# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def kaprekarNumbers(p, q):
    var = False
    if 1 in range(p,q+1):
        print(1,end=" ")
        var = True
    p = max(p,9)
    for i in range(p, q + 1):
        print(end="")
        square = i ** 2
        s = str(square)
        digit = len(s) // 2
        sum = int(s[:digit]) + int(s[digit:])
        if sum == i:
            print(i, end=" ")
            var = True
    if var == False:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = 1
    q = 1000

    kaprekarNumbers(p, q)
