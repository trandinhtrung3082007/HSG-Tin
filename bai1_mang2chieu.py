
m = int(input("Nhap m = "))
n = int(input("Nhap n = "))

a = []

for i in range(0, m):
    a.append([])
    for j in range(0, n):
        x = float(input("Nhap phan tu thu a[%2d][%2d]: " % (i+1, j+1)))
        a[i].append(x)

print("Day so vua nhap la: ")
for i in range(0, m):
    for j in range(0, n):
        print("%3d " % a[i][j], end='')
    print()