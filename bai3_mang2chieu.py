# Input
import numpy as np
m = int(input("Nhập m = ")) # dòng
n = int(input("Nhập n = ")) # cột
a = []
b = []
for i in range(0, m):
    a.append([])
    for j in range(0, n):
        x = int(input("Nhập phần tử a[%s][%s]: " % (i+1, j+1)))
        b.append(x)
        a[i].append(0)
b.sort(reverse=True)

# Tạo biến
hang1 = -1
hang2 = hang1
khong = 0
khong1 = 0
mot = 1
hai = 0
hang3 = -1

# Output
while b!=[]:
    for i in range(khong1,n-khong): # phải sang trái
        a[hang1][hang3] = b[-1]
        b.remove(b[-1])
        hang3 -= 1
    hang3 = hang1-1
    if b == []: 
        break
    for i in range(khong,m-mot):  # duới lên trên
        hang2 -= 1
        a[hang2][khong] = b[-1]
        b.remove(b[-1])
    if b == []: 
        break
    for i in range(khong+1,n-hai):    # trái sang phải
        a[khong][i] = b[-1]
        b.remove(b[-1])
    if b == []: # nhanh nhanh
        break
    for i in range(mot,m-mot):  # trên xuống dưới
        a[i][hang1] = b[-1]
        b.remove(b[-1])
    hang1 -= 1 
    hang2 = hang1
    khong += 1
    khong1+=1
    mot += 1
    hai += 1
print(np.array(a))