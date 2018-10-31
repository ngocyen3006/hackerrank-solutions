# https://www.hackerrank.com/challenges/day-of-the-programmer/problem


def dayOfProgrammer(year):
    if year == 1918:
        return "26.09.1918"

    if (year < 1918) and (year % 4 == 0):
        return "12.09." + str(year)

    if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
        return "12.09." + str(year)

    return "13.09." + str(year)


if __name__ == '__main__':
    year = int(input().strip())

    result = dayOfProgrammer(year)
    print(result)
