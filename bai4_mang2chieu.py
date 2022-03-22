
m = int(input("Nhập m = ")) 
n = int(input("Nhập n = ")) 
a = []
b = []
for i in range(0, m):
    a.append([])
    for j in range(0, n):
        x = float(input("[%2d][%2d]: " % (i+1, j+1)))
        a[i].append(x)

for i in range(0, m):
    for j in range(0, n):
        print("%3d " % a[i][j], end='')
        print()



m1 = int(input("Nhập m1 = ")) 
for i in range(0, m1):
    b.append([])
    for j in range(0, n):
        x = float(input("[%2d][%2d]: " % (i+1, j+1)))
        b[i].append(x)

for i in range(0, m1):
    for j in range(0, n):
        print("%3d " % b[i][j], end='')
        print()


c = a + b
print(c)