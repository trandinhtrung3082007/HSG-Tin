n = int(input())
for i in range(1, n):
    if (n % i == 0):
        print(i, end=",")

sum = 0
for i in range(1, n):
    if (n % i == 0):
        sum += i
 
 
print('tongla', sum)


    
 