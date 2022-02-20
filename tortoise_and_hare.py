def floyd(f, tortoise):
    step = 0
    hare = f(tortoise)
    while tortoise != hare:
        step += 1
        tortoise = f(tortoise)
        hare = f(f(hare))   # The hare moves twice as fast as the tortoise
    return tortoise, step + 1


def brent(f, hare):
    p = 0
    q = 1
    tortoise = f(hare)
    while tortoise != hare:
        if p == q:  # time to start a new power of two?
            hare = tortoise  # The hare jumps !!
            p = 0
            q <<= 1
        tortoise = f(tortoise)
        p += 1
    return hare, p, q


def period(f, x):
    l = [x]
    y = f(x)
    while x != y:
        l.append(y)
        y = f(y)
    return l


class count_calls:
    
    def __init__(self, f):
        self.func = f
        self.calls = 0

    def __call__(self, x):
        self.calls += 1
        return self.func(x)

    
def loop_inc(p):
    return lambda x: x + 1 if x <= p - 2 else 0


def test_floyd(per, pre):
    f = count_calls(loop_inc(per))
    x, p = floyd(f, - pre)
    assert per - 1 - pre % per == x
    assert per + pre - pre % per == p
    assert f.calls == 3 * (p - 1) + 1
    

def test_brent(per, pre):
    f = count_calls(loop_inc(per))
    x, p, q = brent(f, - pre)
    assert (q - pre) % per == x
    assert per == p
    assert max(per, pre) <= q <= 2 * max(per, pre) - 2
    assert f.calls == p + q 
    

def compare_floyd_and_brent():

    powersof2 = [2 ** k for k in range(1, 14)]
    
    print()
    print("Purely periodic case.")
    print()

    print("Period  Floyd == Brent" )
    for p in powersof2:
        f = count_calls(loop_inc(p + 1))
        _, p_brent, _ = brent(f, 0)
        nb_brent = f.calls 
        f.calls = 0
        floyd(f, 0)
        assert nb_brent == f.calls
        print(f"{p_brent:6d}{f.calls:16}")

    print()
    print("Eventually constant case.")
    print()

    f = count_calls(lambda x: x - 1 if x > 0 else 0)
    print("Preperiod  Floyd  Brent  Ratio") 
    for n in powersof2: 
        brent(f, n)
        nb_brent = f.calls
        f.calls = 0
        floyd(f, n)
        nb_floyd = f.calls
        f.calls = 0
        print(f"{n:9}{nb_floyd:7}{nb_brent:7}{nb_floyd/nb_brent:8.4f}")
    
        
n = 300
for q in range(n):
    test_floyd(n - q, q)
    test_brent(n - q, q)

compare_floyd_and_brent()
