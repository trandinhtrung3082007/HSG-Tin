
n=int(input())
tong = 0

if(n%2 == 1):
    for i in range(1,n):
        tong += i

if(n%2 == 0):
    for i in range(1,n):
        tong += i
        
print(tong)