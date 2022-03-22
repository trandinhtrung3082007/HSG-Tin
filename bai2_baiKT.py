n = int(input('n='))
if n<1:
    quit()
elif n>100:
    quit()
lst = []
for i in range(n):
    lst.append(int(input()))
print(lst)
even = filter(lambda n: n % 2 == 0, lst)
odd = filter(lambda n: n % 2 == 1, lst)
a = max(even)
b = min(odd)
if a > b:
    print("Không có số chẵn lớn nhất nhỏ hơn mọi giá trị lẻ")

