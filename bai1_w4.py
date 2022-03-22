n = int(input('n='))
lst = []
for i in range(n):
    lst.append(int(input()))
print('so luong la', len(lst))
answer = 0
for v in lst:
    answer += v

print('tong la', answer)
odd = filter(lambda n: n % 2 == 1, lst)
print('so luong so le la', len(list(odd)))
print(list(reversed(lst)))
print('solonnhatla', max(lst))
print('sonhonhatla', min(lst))
