# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

def kaprekarNumbers(p, q):
    var = False
    for i in range(p, q + 1):
        print(end="")
        square = i ** 2
        s = str(square)
        digit = len(s)
        if digit == 1:
            if square == i:
                print(i, end=" ")
                var = True
        else:
            digit = digit // 2
            l = s[:digit]
            r = s[digit:]
            sum = int(l) + int(r)
            if sum == i:
                print(i, end=" ")
                var = True
    if var == False:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = 1
    q = 300

    kaprekarNumbers(p, q)
