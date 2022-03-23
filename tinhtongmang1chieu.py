n = int(input('n='))
lst = []
for i in range(n):
    lst.append(int(input()))
print(lst)
answer = 0
for v in lst:
    answer += v

print(answer)