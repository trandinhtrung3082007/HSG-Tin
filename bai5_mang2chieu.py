import numpy as np
from numpy.core.fromnumeric import sort
n=int(input())
lap=range(0,n)
num=0
a=[]
if 2<=n<=9:
    for i in lap:
        num=num+1
        a.append(num)
print(np.sort(a))
import itertools
for item in itertools.permutations(a,n):
    print(item)
