n = int(input('n='))
lst = []
for i in range(n):
    lst.append(int(input()))
print(lst)

am = filter(lambda n: n<0, lst)
print(max(list(am)))
a = max(list(am))
