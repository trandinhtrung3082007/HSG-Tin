tong = 0
n = 1
 

 
# Nhập dữ liệu
print("hãy nhập vào số n: ")
n = int(input())
 
# Tính tổng
for i in range(0, n+1):
    tong *= i
 
# In kết quả
print ("Tổng là: ", tong)