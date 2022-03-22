a=int(input()) 

sum = 0
for i in range(1, a+1):
    if (a % i == 0):
        sum += i
print(a, "=", sum)



b=int(input()) 

sum = 0
for i in range(1, b+1):
    if (b % i == 0):
        sum += i
print(b, "=", sum)


while (a,b < 10000):
    if a==b:
        print("Hữu Nghị")
    elif b==a:
        print("Hữu Nghị")
    else:
        print("Không hữu Nghị")
    break