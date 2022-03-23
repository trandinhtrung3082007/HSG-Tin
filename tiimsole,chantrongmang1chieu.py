n = int(input('n='))
lst = []
for i in range(n):
    lst.append(int(input()))
print(lst)
even = filter(lambda n: n % 2 == 0, lst)
odd = filter(lambda n: n % 2 == 1, lst)


print(list(even)) 
print(list(odd))