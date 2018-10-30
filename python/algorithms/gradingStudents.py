# https://www.hackerrank.com/challenges/grading/problem

def gradingStudents(grades):
    for i in range(len(grades)):
        if (grades[i] % 10 == 3 or grades[i] % 10 == 8) and grades[i] + 2 >= 40:
            grades[i] = grades[i] + 2
            continue
        if (grades[i] % 10 == 4 or grades[i] % 10 == 9) and grades[i] + 1 >= 40:
            grades[i] = grades[i] + 1
            continue
    return grades


if __name__ == '__main__':
    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(*result, sep='\n')
