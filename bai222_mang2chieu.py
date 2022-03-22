nhap = input()
nhap = nhap.split(' ')
while len(nhap)!=2 or int(nhap[1])<1 or int(nhap[1])>int(nhap[0]) or int(nhap[0])>10**9:
	nhap = input("Nhập lại: ")
	nhap = nhap.split(' ')
a = int(nhap[0])
b = int(nhap[1])
ketqua = 0
while b!=a:
	c = a
	a = b
	b = c-b
	if b>a:
		c = a
		a = b
		b = c
	ketqua += 1
print(ketqua+1)
