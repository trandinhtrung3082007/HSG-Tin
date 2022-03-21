n = int(input('n='))
lst = []
for i in range(n):
    lst.append(int(input()))

print(min(lst))
m = min(lst)
vt = lst.index(m)
print(vt)