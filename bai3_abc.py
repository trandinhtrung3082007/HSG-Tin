a = []
n=int(input("N: "))
for i in range(1,n):
    i = int(input("Nhập số: "))
    a.append(i)

b = []
for j in range(len(a)-1): 
    b.append(a.count(a[i]))

c = []
for j in range(len(b)-1):
    if b[j] == max(b):
        c.append(a[j])

s = set(a)
e = list(s)
print("Dãy số: ",a)
print('gia tri xuat hien nhieu nhat = ',c[0])
print("Giá trị khác nhau: ",len(e))