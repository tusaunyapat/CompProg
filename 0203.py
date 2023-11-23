#python 0203.py

data = str(input())
data = data.split("/")
print(data)

month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

print(month[int(data[1])-1],end=' ')
print(data[0],end='')
print(',', end=' ')
print(data[2])