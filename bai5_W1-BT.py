def totalDigitsOfNumber(a):
    total = 0;
    while (a > 0):
        total = total + a % 10;
        a = int(a / 10);
    return total;
 
a = input();
print(totalDigitsOfNumber(a))
