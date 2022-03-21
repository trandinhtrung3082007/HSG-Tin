a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
m = int(input('m='))
max = a*b
if (a*c >max):
    max=a*c
if (b*c >max):
    max=b*c
print(max%m)