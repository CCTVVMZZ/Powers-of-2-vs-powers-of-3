period = 480720240 
for modulus in range(2, 80):
    if modulus == 48:
        (m, n) = (5, 4)
    elif modulus in [27, 54]:
        (m, n) = (9, 3)
    elif modulus in [16, 32, 64]:
        (m, n) = (6, 0)
    else:
        (m, n) = (3, 2)
    p2 = pow(2, m, modulus)
    p3 = pow(3, n, modulus)
    assert (pow(2, m + period, modulus) - p2) % modulus  == 0
    assert (pow(3, n + period, modulus) - p3) % modulus == 0
    assert (p3 - p2 - 1) % modulus == 0
    print(modulus, end = " ")
    
