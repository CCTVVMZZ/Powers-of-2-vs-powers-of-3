"""
That module contains two functions called \"floyd\" and \"brent\", respectively.
Each implements a cycle detection algorithm based on the \"tortoise and hare\" strategy.
The code is adapted from wikipedia:

https://en.wikipedia.org/w/index.php?title=Cycle_detection&oldid=1067069441
"""

def floyd(f, x0):
    """ 
    An implementation of Floyd's \"tortoise and hare\" algorithm.
    It returns a tuple (preperiod, period) of lists.
    """

    tortoise = f(x0) 
    hare = f(tortoise)
    while tortoise != hare:
        tortoise = f(tortoise)
        hare = f(f(hare))   # The hare moves twice as fast as the tortoise
  
    preperiod = []
    tortoise = x0    # The tortoise is reset
    while tortoise != hare:
        preperiod.append(tortoise)
        tortoise = f(tortoise)
        hare = f(hare)   # The hare and tortoise move at same speed
 
    period = [tortoise] 
    hare = f(tortoise)
    while tortoise != hare:
        period.append(hare)
        hare = f(hare)   # The tortoise stay still
 
    return preperiod, period


def brent(it):
    it = iter(it)
    q = p = 1
    hare = next(it)
    tortoise = next(it)
    while tortoise != hare:
        if p == q:  # time to start a new power of two?
            hare = tortoise  # The hare jumps !!
            q <<= 1
            p = 0
        tortoise = next(it)
        p += 1
    return tortoise, p

def floyd(f, x1):
    p = 1
    tortoise = x1 
    hare = f(x1)
    while tortoise != hare:
        p += 1
        tortoise = f(tortoise)
        hare = f(f(hare))   # The hare moves twice as fast as the tortoise
    return tortoise, p

def brent(f, x1):
    q = p = 1
    hare = x1
    tortoise = f(x1)
    while tortoise != hare:
        if p == q:  # time to start a new power of two?
            hare = tortoise  # The hare jumps !!
            q <<= 1
            p = 0
        tortoise = f(tortoise)
        p += 1
    return hare, p

def iter_func(f, x):
    while True:
        yield x
        x = f(x)

from itertools import cycle

def iter_eventually_periodic(q, p):
    yield from range(q + p - 1, p - 1, -1)
    yield from cycle(range(p))

def func_eventually_periodic(p):
    def f(n):
        if n > 0:
            return n - 1
        return p - 1
    return f

# m = 81 * 7
# b = 3
# mule = lambda x: (b * x) % m
# print(floyd(mule, 1))
# print(brent(iter_func(mule, 1)))


print()
#for p in [5, 9, 17, 33, 65]:
for p in [3, 7, 15, 31, 63]:
    f = lambda x: (x + 1) % p
    print(brent(f, 0), "|", floyd(f, 0))


# for p in [4, 8, 16, 32, 64]:    
#     print(brent(iter_eventually_periodic(p - 1, 1)), "*", 
#           floyd(func_eventually_periodic(1), p))

