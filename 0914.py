c = input()
t = input()
d = input()

d_course, d_teacher = {}, {}

course = open(c, 'r')
for line in course:
    num,code = line.strip().split(',')
    d_course[num] = code
print(d_course)
course.close()

teacher = open(t, 'r')
for line in teacher:
    num,code = line.strip().split(',')
    d_teacher[num] = code
print(d_teacher)
teacher.close()

database = open(d, 'r')
for line in database:
    codeCourse, codeTeacher = line.strip().split(',')
    if codeCourse in d_course and codeTeacher in d_teacher:
        print(d_course[codeCourse]+','+d_teacher[codeTeacher])
    else :
        print('record error')

