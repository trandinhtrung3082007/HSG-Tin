a = int(input())
b = int(input())
def u(a, b):
    temp1 = a
    temp2 = b
    while (temp1 != temp2):
        if (temp1 > temp2):
            temp1 -= temp2
        else:
            temp2 -= temp1
    uscln = temp1
    return uscln
    
print (u(a, b))