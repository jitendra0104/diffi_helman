def power(a, b, p):
    if b == 1:
        return a
    else:
        return pow(a, b) % p

def diffe_helman():
    g = 9
    p = 23
    x = 3
    y = 5
    
    k1 = power(g, x, p)
    k2 = power(g, y, p)
    print("Shared key for Alice is:", k1)
    print("Shared key for Bob is:", k2)

    shared_key = power(k2, x, p)
    print("Shared secret key is:", shared_key)
