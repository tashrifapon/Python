#******************************************************************************
# yield.py
#******************************************************************************
# Name: Tashrif Apon
#******************************************************************************
# Remarks (optional):
# works with test case
# much easier than it seemed at first
# ^ but i didn't do the challenge (seems hard or tedious or both)
b = float(input('Enter B: '))
c1 = float(input('Enter c1: '))
c2 = float(input('Enter c2: '))
c3 = float(input('Enter c3: '))
t1 = float(input('Enter T1: '))
t2 = float(input('Enter T2: '))
t3 = float(input('Enter T3: '))

import math
def fn(x):
    return c1*math.exp(-x*t1) + c2*math.exp(-x*t2) + c3*math.exp(-x*t3) - b
def drv_fn(x):
    return -t1*c1*math.exp(-x*t1) + -t2*c2*math.exp(-x*t2) + -t3*c3*math.exp(-x*t3)

x = 0.1
for i in range(100):
    x -= fn(x)/drv_fn(x)
    if abs(fn(x)) < 10**(-8):
        print(f'x = {x:.7f}, so {100*x:.2f}%')
        print(f'It took {i} tries')
        break      
