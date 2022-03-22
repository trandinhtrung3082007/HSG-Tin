import numpy as np
def bai22():
    try:
        a=[]
        dung = 0
        ketqua = []
        
        M=int(input("M: "))
        N=int(input("N: "))
        
        for i in range (0,M):
            tr = []
            
            for j in range (0,N):
                t = int(input("Phần tử " + str(i) + "-" + str(j) + ": "))#Yên Ngựa của hàng và cột a
                tr.append(t)

            a.append(tr)

        for i in range(0,M):
            for g in range(0,N):

                if a[i][g] == np.min(a[i]):

                    for t in range(0,M):

                        if a[t][g] > a[i][g]:
                            dung += 1
                            
                    if dung==0:
                        ketqua.append(str(a[i][g]))
                    else:
                        dung = 0

                elif a[i][g] == np.max(a[i]):
                    for t in range(0,M):
                        if a[t][g] < a[i][g]:
                            dung += 1

                    if dung==0:
                        ketqua.append(str(a[i][g]))
                    else:
                        dung = 0

        if len(ketqua)!=0:
            print('''Các phần tử "yên ngựa" là''',', '.join(ketqua))
        else:
            print('''Không có phần tử "yên ngựa"''')

    except:
        print("Chỉ được nhập từng số")
bai22()

 