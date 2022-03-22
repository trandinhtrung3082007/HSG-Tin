import math as m
import numpy as np
from fractions import*

n = int(input())
def bai1():
    def A():
        mang = []
        if 1<=n<=32000:
            for i in range(0,n):
                i = i + 1
                A = m.sqrt(i)
                mang.append(A)
            print(np.sum(mang))
    
    def B():
        try:
            if 1<=n<=32000:
                for i in range(0,n):
                    pt1 = Fraction(1,i+1)
                    pt2 = Fraction(1,i+2)
                    pt3 = Fraction(1,i+3)
                    B =  pt1 + pt2 - pt3
                    tinh = m.sqrt(1) - m.sqrt(B)
                print(tinh)

        except ZeroDivisionError:
            z = 0
            print(z)

    if __name__ and "___main___":
        B()
5