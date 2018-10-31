# https://www.hackerrank.com/challenges/bon-appetit/problem

def bonAppetit(bill, k, b):
    actual = (sum(bill) - bill[k]) // 2
    if actual == b:
        print("Bon Appetit")
        return

    print(b - actual)


if __name__ == '__main__':
    nk = input().rstrip().split()
    n = int(nk[0])
    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())

    bonAppetit(bill, k, b)
