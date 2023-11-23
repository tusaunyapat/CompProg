n = int(input())

win = set()
lose = set()

for i in range(n):
    WIN, LOSE = input().split()
    win.add(WIN)
    lose.add(LOSE)

winner = win - lose
print(sorted(winner))