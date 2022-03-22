n = int(input())
def phanTichSoNguyen(n):
    i = 2;
    l = [];
    while (n > 1):
        if (n % i == 0):
            n = int(n / i);
            l.append(i);
        else:
            i = i + 1;
    if (len(l) == 0):
        l.append(n);
    return l;
 

listNumbers = phanTichSoNguyen(n)
size = len(listNumbers)
sb = "";
for i in range(0, size - 1):
    sb = sb + str(listNumbers[i]) + " x "
sb = sb + str(listNumbers[size-1])
print(n, "=", sb);