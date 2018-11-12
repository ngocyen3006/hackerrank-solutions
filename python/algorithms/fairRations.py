# https://www.hackerrank.com/challenges/fair-rations/problem

def fairRations(B):
    loaf = 0
    for i in range(len(B) - 1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i + 1] += 1
            loaf += 2
    if B[-1] % 2 == 1:
        return "NO"
    return loaf
