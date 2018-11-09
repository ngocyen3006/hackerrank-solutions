# https://www.hackerrank.com/challenges/halloween-sale/problem

def howManyGames(p, d, m, s):
    game = 0
    cost = p
    while cost <= s:
        p = max(p - d, m)
        cost += p
        game += 1
    return game


if __name__ == '__main__':
    pdms = input().split()
    p = int(pdms[0])
    d = int(pdms[1])
    m = int(pdms[2])
    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)
    print(answer)
