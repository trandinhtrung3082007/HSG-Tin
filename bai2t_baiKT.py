A = list(map(int, input().split()))
chan = []
le = []
for i in range(0,len(A)):
    ds = A[i]
    if ds % 2:
        le.append(ds)
    else:
        chan.append(ds)
for q in range(0,len(chan)):
    a = chan[q]
for j in range(0,len(le)):
    b = le[j]
if a < b:
    print("Số chẵn lớn nhất nhỏ hơn mọi số lẻ:",a)
else:
    print("Không có số chẵn nào lớn nhất nhỏ hơn mọi số lẻ")