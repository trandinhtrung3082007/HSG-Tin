f = open('dayso.inp','r')
f2 = open('dayso,out','w')
dayso = f.read()
dayso = dayso.split()
mang = []
for i in range(len(dayso)):
    mang.append(int(dayso[i]))
a = mang[0]
b = mang[1]
c = mang[2]
m = mang[3]
max = a*b
if (a*c >max):
    max=a*c
if (b*c >max):
    max=b*c
f2.write(str(max%m))