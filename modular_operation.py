def gcd(a,b):
    while b:
        a, b = b, a % b
    return a    

def modular_inverse_tabular_approach(phi, e):
    a=[1,0]
    b=[0,1]
    z=[phi,e]
    k=[0, phi//e]
    i=2
    while z[-1] != 1:
        a.append(a[i - 2] - (a[i - 1] * k[i - 1]))
        b.append(b[i - 2] - (b[i - 1] * k[i - 1]))
        z.append(z[i - 2] - (z[i - 1] * k[i - 1]))
        k.append(z[i-1]//z[i])
        i += 1

    return b[-1] % phi if b[-1] > 0 else (b[-1] + phi) % phi

print(modular_inverse_tabular_approach(20,7))
print(gcd(2,1))
