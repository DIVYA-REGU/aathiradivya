n=int(input())
students=[]
for i in range(n):
    name=input()
    score=float(input())
students.append([name,score])
students.sort(key=lambda x:x[1])
second_lowest_grade = None
for student in students:
  if second_lowest_grade is None or student[1] > second_lowest_grade:
            second_lowest_grade = student[1]

    # Find students with the second lowest grade
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]















for student in students:
    if second_lowest_grade is None or student[1] < second_lowest_grade:
        second_lowest_grade = student[1]
        break
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
second_lowest_students.sort()
for student in second_lowest_students:
        print(student)
