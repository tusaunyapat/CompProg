#python 0206.py

v1 = input()[1:-1].split(',')
v2 = input()[1:-1].split(',')


v3 = [float(v1[0])+float(v2[0]), 
      float(v1[1])+float(v2[1]),
      float(v1[2])+float(v2[2])]

for i in range(3):
    v1[i] = float(v1[i])
    v2[i] = float(v2[i])

# print(v1[0],v1[1],v1[2])
# print(v2[0],v2[1],v2[2])
print(v1,'+',v2,'=',v3)
