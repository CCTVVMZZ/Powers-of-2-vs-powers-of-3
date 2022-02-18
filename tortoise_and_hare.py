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
    return hare, q, p

class count_calls:
    def __init__(self, f):
        self.func = f
        self.calls = 0

    def __call__(self, x):
        self.calls += 1
        return self.func(x)

def eventually_periodic(q, p):
    def f(x):
        x += 1
        if x == p + q: return q
        return x 
    return f

powersof2 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]

print()
print("Purely periodic case.")
print()
print("Period  Floyd  Brent" )
for p in powersof2:
    f = count_calls(lambda x: (x + 1) % (p + 1))
    _, _, p_brent = brent(f, 0)
    nb_brent = f.calls 
    f.calls = 0
    _, p_floyd = floyd(f, 0)
    assert p_brent == p_floyd
    print(f"{p_brent:6d}{f.calls:7}{nb_brent:7}")
    
print()
print("Eventually constant case.")
print()

f = count_calls(lambda x: x - 1 if x > 0 else 0)
print("Preperiod  Floyd  Brent  Ratio") 
for p in powersof2: 
    brent(f, p - 1)
    nb_brent = f.calls
    f.calls = 0
    floyd(f, p - 1)
    nb_floyd = f.calls
    f.calls = 0
    print(f"{p:9}{nb_floyd:7}{nb_brent:7}{nb_floyd/nb_brent:7.3f}")

