# Crible d'Ératosthène


def Cribe(M) :
    L = [True] * (M+1)
    prime = []
    
    if M >= 0 :
        L[0] = False
    if M >= 1 :
        L[1] = False
    if M >= 2 :
        lprime = 2
        prime.append(2)
        while lprime**2 <= M :
            for i in range(lprime, (M-1) // lprime + 1) :
                L[i * lprime] = False
            
            lprime += 1
            while not L[lprime] :
                lprime += 1
            prime.append(lprime)
            print("Add", lprime)
        
        lprime += 1
        while lprime <= M :
            while not L[lprime] :
                lprime += 1
            prime.append(lprime)
            lprime += 1
    return prime


def Eras(M) :
    L = [True] * (M + 1)
    L[0] = False
    L[1] = False
    i = 2
    
    while i <= M :
        while i <= M and not L[i] :
            i += 1
        
        j = i*i
        while j <= M :
            L[j] = False
            j += i
        i += 1
    
    return L

def PtPrem(M) :
    L = Eras(M)
    P = []
    for i in range(0, M+1) :
        if L[i] :
            P.append(i)
    return P

from time import clock

deb = clock()
PREMIER = Cribe(10**9)
fin = clock()
print("temps de calcul =", fin - deb, "secondes")


def Bezout(a, b) :
    r0 = abs(a)
    r1 = abs(b)
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
    
    while r1 > 0 :
        (r0, r1) = (r1, r0 - r0 // r1 * r1)
        (u0, u1) = (u1, u0 - r0 // r1 * u1)
        (v0, v1) = (v1, v0 - r0 // r1 * v1)
    
    if a < 0 :
        u0 = -u0
    if b < 0 :
        v0 = -v0
    return (r0, u0, v0)

def ResolvCongr(R, M) :
    x = R[0]
    prod = M[0]
    
    for i in range(1, len(M)) :
        (_, u, v) = Bezout(prod, M[i])
        x = M(i] * v * x + prod * u * R[i]
        prod *= M[i]
        x %= prod
    
    return x
    