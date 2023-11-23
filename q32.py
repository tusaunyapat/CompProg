num = input().split()
n, m, k = int(num[0]), int(num[1]), int(num[2])
all_fac = []
student = {}

for i in range(n):
    stu, fac = input().split()
    student[stu] = fac
    all_fac.append(fac)

guests = {}
for i in range(m):
    people = input().split()
    guest = people[0]
    guests[guest] = people[1:]

for i in range(k): #ALL
    meet = input().split()
    ans = set(all_fac)
    for i in meet: #line
        # print(guests[i])
        s = set()
        for j in guests[i]:
            s.add(student[j])
        ans = ans & s
    if ans == set():
        print('None')
    else:
        print(' '.join(list(ans)))


