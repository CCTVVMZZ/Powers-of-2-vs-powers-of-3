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
            
    return pos, neg
        
