n = int(input())
students = []
for _ in range(n):
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    students.append([name, score])
students.sort(key=lambda x: x[1])
second_lowest_grade = None
for student in students:
    if second_lowest_grade is None or student[1] > second_lowest_grade:
        second_lowest_grade = student[1]
        break
second_lowest_grade = None
for student in students:
    if second_lowest_grade is None or student[1] > second_lowest_grade:
        second_lowest_grade = student[1]
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
second_lowest_students.sort()
for student in second_lowest_students:
    print(student)
