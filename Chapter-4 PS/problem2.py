marks = []
num_students = 6
for i in range(num_students):
    mark = float(input(f"Enter the marks of students: {i + 1} "))
    marks.append(mark)

print(marks)

marks.sort()
print(marks)
