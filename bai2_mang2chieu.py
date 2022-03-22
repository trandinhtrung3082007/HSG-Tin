import numpy as np
def spiralPrint(m, n, a):
    k = 0
    l = 0
 
    ''' k - starting row index
        m - ending row index
        l - starting column index
        n - ending column index
        i - iterator '''
 
    while (k < m and l < n):
 
        # Print the first row from
        # the remaining rows
        for i in range(l, n):
            print(a[k][i], end=" ")
 
        k += 1
 
        # Print the last column from
        # the remaining columns
        for i in range(k, m):
            print(a[i][n - 1], end=" ")
 
        n -= 1
 
        # Print the last row from
        # the remaining rows
        if (k < m):
 
            for i in range(n - 1, (l - 1), -1):
                print(a[m - 1][i], end=" ")
 
            m -= 1
 
        # Print the first column from
        # the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                print(a[i][l], end=" ")
 
            l += 1
 
 
a=[]
R=int(input("m: "))
C=int(input("n: "))
for i in range (0,R):
    temp_row = []
    for j in range (0,C):
        temp=int(input("Phần tử " + str(i) + "-" + str(j) + ": "))
        temp_row.append(temp)
    a.append(temp_row)
a=np.array(a)

spiralPrint(R, C, a)