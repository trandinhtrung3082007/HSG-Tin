snt = open("D:/IT/pythonfile/nhapxuatfile/CAU1.INP", "r")
ketqua = open("D:/IT/pythonfile/nhapxuatfile/CAU1.OUT", "w")
snt2 = snt.read()

def check(n):
    kq = 1
    if (n < 2):
        kq = 0
        return kq
    for p in range(2, n):
        if n % p == 0:
            kq = 0
            break
    return kq

mang = []
for i in range(0,int(snt2)):
    i += 1
    if check(i) == 1:
        mang.append(i)
kq = []
for j in range(0,len(mang)):
    a = mang[j]
    b = mang[j-1]
    tong = a + b
    if tong == int(snt2):
        print(a)
        print(b)
        ketqua.write(str(a))
        ketqua.write("\n")
        ketqua.write(str(b))
