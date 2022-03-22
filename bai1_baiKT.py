n = int(input())
if n<0:
    print("nhập lại")
    quit()
elif n>65535:
    print("nhập lại")
    quit()
#b
def tongcacchuso(n):
        a = 0
        while (n > 0):
            a = a + n % 10
            n = int(n / 10)
        return a
print(tongcacchuso(n))
#c

def phanTichSoNguyen(n):
    i = 2;
    listNumbers = []
    while (n > 1):
        if (n % i == 0):
            n = int(n / i)
            listNumbers.append(i)
        else:
            i = i + 1
    if (len(listNumbers) == 0):
        listNumbers.append(n)
    return listNumbers
listNumbers = phanTichSoNguyen(n);
size = len(listNumbers)
sb = "";
for i in range(0, size - 1):
    sb = sb + str(listNumbers[i]) + " x "
sb = sb + str(listNumbers[size-1])

print("Kết quả:", n, "=", sb)
#a
count=0
while(n>0):
    count=count+1
    n=n//10
print(count)