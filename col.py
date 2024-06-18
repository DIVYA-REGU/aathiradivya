from collections import namedtuple
n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
students = [Student(*input().split()) for _ in range(n)]
average_marks = sum(float(student.MARKS) for student in students) / n
print("{:.2f}".format(average_marks))
