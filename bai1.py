n = int(input('n='))
lst = []
for i in range(n):
    lst.append(int(input()))
even = filter(lambda n: n % 2 == 0, lst)
odd = filter(lambda n: n % 2 == 1, lst)


print(list(even)) 
print(list(odd))
s = 0
for i in range(n):
    if lst[i]%2 == 1:
        s = s+lst[i]
print(s)
for i in range(n-1,-1,-1):
    if lst[i]>0:
        lst.remove(lst[i])
print(lst)
