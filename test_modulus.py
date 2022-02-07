def tortoise_and_hare(x0, f):
    t = f(x0)
    h = f(f(x0))
    while t != h:
        t = f(t) 
        h = f(f((h)))
    preperiod = []
    t = x0
    while t != h:
        preperiod.append(t)
        t = f(t)
        h = f(h)
    period = [t]
    h = f(t)
    while t != h:
        period.append(h)
        h = f(h) 
    return preperiod, period

def powers(b, m):
    t = b = b % m
    h = b2 = (b * b) % m
    while t != h:
        t = (b * t) % m
        h = (b2 * h) % m
    Q = []
    t = 1
    while t != h:
        Q.append(t)
        t = (b * t) % m
        h = (b * h) % m
    P = [t]
    h = (b * t) % m
    while t != h:
        P.append(h)
        h = (b * h) % m
    return Q, P

def smallest_nonegative_difference(X, Y):
    smallest_so_far = X[-1] - Y[0]
    if smallest_so_far < 0:
        raise ValueError("All differences are negative !!!")
    i = 0
    j = 0
    while (i < len(X)) and (j < len(Y)):
        d = X[i] - Y[j]
        if d < 0:
            i += 1
        else:
            smallest_so_far = min(d, smallest_so_far)
            j += 1
    return smallest_so_far
    
    

def test_modulus(m):
    Q2, P2 = powers(2, m)
    Q3, P3 = powers(3, m)
    P2.sort()
    P3.sort()
    
    pos = P2[-1]
    i2 = 0
    i3 = 0
    while (i2 < len(P2)) and (i3 < len(P3)):
        d = P2[i2] - P3[i3]
        if d >= 0:
            if pos > d:
                pos2 = P2[i2]
                pos3 = P3[i3]
                pos = d
            i3 += 1
        else:
            i2 += 1
            
    neg = - P3[-1]
    i2 = 0
    i3 = 0
    while (i2 < len(P2)) and (i3 < len(P3)):
        d = P2[i2] - P3[i3]
        if d <= 0:
            if neg < d:
                neg2 = P2[i2]
                neg3 = P3[i3]
                neg = d
            i2 += 1
        else:
            i3 += 1
            
    return len(Q2), len(Q3), pos, neg

        
def brutal_test(modulus, p2min, p2max, p3min, p3max, rmin, rmax):
    assert pow(2, p2min, modulus) == pow(2, p2max, modulus)
    assert pow(3, p3min, modulus) == pow(3, p3max, modulus)
    for p2 in range(p2min, p2max):
        for p3 in range(p3min, p3max):
            for r in range(rmin, rmax):
                assert (pow(2, p2, modulus) - pow(3, p3, modulus) - r) % modulus != 0 
