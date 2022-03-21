#file tự nhập
dong1 = "minhquang02"
dong2 = "huyen20"

from operator import le
import re
loc = re.findall(r'\d', dong1)
loc2 = re.findall(r'\d', dong2)

mang1 = []
mang2 = []

for i in range(0,len(loc)):
    a = loc[i] + loc[i-1]
    mang1.append(int(a))

for j in range(0,len(loc)):
    b = loc2[j] + loc2[j-1]
    mang2.append(int(b))

mang3 = []

for f in range(0,len(mang1)):
    ss1 = mang1[f]
    for q in range(0,len(mang2)):
        ss2 = mang2[q]
        if ss1 == ss2:
            mang3.append(ss1 or ss2)
print(max(mang3))
