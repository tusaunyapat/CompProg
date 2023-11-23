n = int(input())

department = {}
for i in range(n):
    park, num = input().split()
    department[park] = int(num)

students = []
n = int(input())
for i in range(n):
    ID, score, p1, p2, p3, p4 = input().split()
    students.append([float(score), ID, p1, p2, p3, p4])

students.sort(reverse=True)
ans = []
for i in range(n):
    for j in range(4):
        if department[students[i][j+2]] != 0:
            ans.append([students[i][1],students[i][j+2]])
            department[students[i][j+2]] -= 1
            break
ans.sort()
[print(ID, p) for ID, p in ans]
