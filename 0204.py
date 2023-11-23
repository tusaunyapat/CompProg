#python 0204.py

m = input()
n = int(input())

num = n - len(m)

if num>0:
    for i in range(num):
        print('0',end='')

print(m)
