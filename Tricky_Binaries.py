import math
import os
import re
import sys

def seeBin(n):
    Rem = list()
    if n%2 == 0:
        Rem.append(0)
        n = n/2
        while n >= 2:
            if n%2 == 0:
                Rem.append(0)
                n = n/2
            else:
                Rem.append(1)
                n = (n-1)/2
        Rem.append(1)
    else:
        Rem.append(1)
        n = (n-1)/2
        while n>= 2:
            if n%2 == 0:
                Rem.append(0)
                n = n/2
            else:
                Rem.append(1)
                n = (n-1)/2
        Rem.append(1)
    count_one(Rem)

def count_one(Rem):
    l1, l2 = Rem, Rem
    max_one, cons = 1, 1
    for i in range(len(l1)-1):
        if (l1[i] + l2[i+1]) == 2:
            cons += 1
            if cons > max_one:
                max_one = cons
        else:
            cons = 1
    print(max_one)

if __name__ == '__main__':
    n = int(input())
    if n < 1000000:
        seeBin(n)
