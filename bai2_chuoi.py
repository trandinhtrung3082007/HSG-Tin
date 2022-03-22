import re
n = input()
m1 = re.findall(r'\d+', n)  
print(m1)