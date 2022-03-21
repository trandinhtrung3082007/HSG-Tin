#tinh tong 1/1+1/2+1/3+...+1/n
tong = 0
n = 0
 
print("Hãy nhập vào số n: ")
n = int(input())
 
for i in range(1, n + 1) :
    tong += 1 / i
 
print("Tổng số là: ", tong)