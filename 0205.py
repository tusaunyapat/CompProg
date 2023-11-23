#python 0205.py

data = input()
data = data.split()
answer = 0

for i in data:
    answer += int(i)

print(answer)