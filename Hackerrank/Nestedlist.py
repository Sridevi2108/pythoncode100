if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))
    grades = sorted(set(score for _, score in students))
    second_lowest = grades[1]
    result = [name for name, score in students if grades == second_lowest]
    for name in sorted(result):
        print(name)









