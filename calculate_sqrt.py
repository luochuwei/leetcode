#-*- coding: utf-8 -*-
def f(n):
    """
    牛顿法求n的平方根,
    https://zh.wikipedia.org/wiki/%E7%89%9B%E9%A1%BF%E6%B3%95
    """
    x = 1.0
    while abs(x*x-n) > 1e-9:
        x = x - (x*x-n)/(2.0*x)
    return x

print f(100)
print f(4)
print f(1.23), pow(1.23, 0.5)


def g(x):
    """二分法"""
    low = 0
    high = x
    guess = (low + high)/2.0
    counter = 1

    while abs(guess **2 - x) > 1e-9 and counter <= 100:
        if guess**2 < x:
            low = guess
        else:
            high = guess
        guess = (low + high)/2.0
        counter += 1
    return guess


print g(100)
print g(1.23)