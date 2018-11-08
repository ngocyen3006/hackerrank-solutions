# https://www.hackerrank.com/challenges/dynamic-array/problem

def dynamicArray(n, queries):
    s = [[] * n for _ in range(n)]
    lastAnswer = 0
    for i in queries:
        if i[0] == 1:
            index = (i[1] ^ lastAnswer) % n
            s[index].append(i[2])
            continue
        if i[0] == 2:
            index1 = (i[1] ^ lastAnswer) % n
            index2 = i[2] % len(s[index1])
            lastAnswer = s[index1][index2]
            print(lastAnswer)
    pass


if __name__ == '__main__':
    queries = []
    with open("dynamicArrayTest.txt") as file:
        line = file.readline()
        nq = line.rstrip().split()
        n = int(nq[0])
        q = int(nq[1])
        line = file.readline()
        while line:
            queries.append(list(map(int, line.rstrip().split())))
            line = file.readline()

    dynamicArray(n, queries)
