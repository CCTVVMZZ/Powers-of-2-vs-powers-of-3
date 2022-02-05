def ultimate_powers(b, m):
    t = 1
    h = b % m
    c = (b * b) % m
    while t != h:
        t = (b * t) % m
        h = (c * h) % m
    P = [t]
    h = (b * t) % m
    while t != h:
        P.append(h)
        h = (b * h) % m
    return P

def test_modulus(m, D):
    P2 = ultimate_powers(2, m)
    P3 = ultimate_powers(3, m)
    for d in D:
        for p3 in P3:
            if d + p3 in P2:
                return False 
    return True
            
#q =  (2 ** 15) * (2 ** 8 + 1) * (2 ** 16 + 1) #(-7153, 6487)  
#q = (2 ** 9) * 17 * 257 #(-139, 269)
q = (3 ** 5) * (3 ** 12 + 1)
#D = list(range(- 100,  101))
#print(test_modulus(q, D))
P2 = ultimate_powers(2, q)
P3 = ultimate_powers(3, q)
D = { p2 - p3 for p2 in P2 for p3 in P3 }
D = list(D)
D.sort()
# assert min(D) > - q
# assert max(D) < q
print((max(d for d in D if d <= 0), min([d for d in D if d >= 0])))
# for q in range(16 * 257, 17 * 257):
#     if q % 100 == 0: print(q)
#     if
#         print("OK")
#         print(q)
#         break
# # S = set()
# # for r in range(1, 1000):
# #     q = (2 ** 9) * r 
# #     if q % 3 != 0:
# #         P2 = ultimate_powers(2, q)
# #         if P2 == [0]: continue
# #         P3 = ultimate_powers(3, q)
# #         D = { p2 - p3 for p2 in P2 for p3 in P3 }
# #         D = list(D)
# #         D.sort()
# #         assert min(D) > - q
# #         assert max(D) < q
# #         #print(f"{q = }")
# #         S.add((max(d for d in D if d <= 0), min([d for d in D if d >= 0])))
# #         if r % 100 == 0 : print(S)

# # print(S)

#128 - 27  = 101
