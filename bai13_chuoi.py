def findSum(str1, str2):
     
    if (len(str1) > len(str2)):
        t = str1
        str1 = str2
        str2 = t
 
    str = ""
 
    n1 = len(str1)
    n2 = len(str2)
 
    str1 = str1[::-1]
    str2 = str2[::-1]
 
    carry = 0;
    for i in range(n1):
         
        sum = ((ord(str1[i]) - 48) +
              ((ord(str2[i]) - 48) + carry))
        str += chr(sum % 10 + 48)
 
        carry = int(sum / 10)
 
    for i in range(n1, n2):
        sum = ((ord(str2[i]) - 48) + carry)
        str += chr(sum % 10 + 48)
        carry = (int)(sum / 10)
 
    if (carry):
        str += chr(carry + 48)
    str = str[::-1]
 
    return str
 

str1 = "1240524387987587983747847368975847982783568547867485379018015454329123875637289193739857289798347273578675437843857971710451435135324534621155"
str2 = "19881467281992876918798176767565365326756751818786762652411544165515141541280984098390850067473626165617847997311"
print(findSum(str1, str2))
 