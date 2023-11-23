a = 0
grades = ['A','B+','B','C+','C','D+','D','F']
student = []
grade = []
i = 0

while a!='q':
    # student[i],grade[i] = input().split()
    a = input()
    if a =='q':
        break
    b,c = a.split()
    student.append(b)
    grade.append(c)
    i+=1

want = input().split()

for i in range(len(want)):
    indexStudent = student.index(want[i])
    indexGrade = grades.index(grade[indexStudent])
    if indexGrade!=0:
        grade[indexStudent] = grades[indexGrade-1]

for i in range(len(student)):
    print(student[i], grade[i])
