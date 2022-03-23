a = int(input())
b = int(input())
def ucln(a, b):
    r=a%b
    while r !=0:
        a=b
        b=r
        r=a%b
        return b
        break
print(ucln(a, b))