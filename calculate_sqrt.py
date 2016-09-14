#-*- coding: utf-8 -*-
def f(n):
    """
    牛顿法求n的平方根
    """
    x = 1.0
    while abs(x*x-n) > 1e-9:
        x = x - (x*x-p)/(2.0*x)
    return x

print f(100)
print f(4)
print f(1.23), pow(1.23, 0.5)