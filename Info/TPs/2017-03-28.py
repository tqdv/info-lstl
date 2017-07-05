"""
Permutations
"""

"""
def EstPermutation(l) :
    st = [0] * len(l)
    for i in l :
        if i < 0 or i > len(l) -1 :
            return False
        else :
            st[i] +=1
            if st[i] > 1 :
                return False
    for i in st :
        if i == 0 :
            return False
    return True
"""

def Id(n) :
    return list(range(n))


def EstPermutation(l) :
    n = len(l)
    
    T = [False] * n
    
    for x in l :
        if 0 <= x < n :
            t[x] = True
        else :
            return False
    
    for b in T :
        if b == False :
            return False
    
    return True

def J(n) :
    return range(n)

def Composee(sigma, rho) :
    n = len(sigma)
    assert len(rho) == n
    
    comp = [0] * n
    
    for x in range(n) :
        comp[x] = sigma[rho[x]]
    
    return comp

def Puissance(sigma, k) :
    n = len(sigma)
    rho = Id(n)
    
    for _ in range(k) :
        rho = Composee(rho, sigma)
    
    return rho

def Inv(sigma) :
    n = len(sigma)
    
    f = [0] * n
    
    for x in range(n) :
        f[sigma[x]] = x
    
    return f

"""
Partie 2 : Exemlpes de permutation
"""

"""
Une transposition est une permutation qui échange juste 2 éléms.
Celle qui échange i et j se note souvent (i j)
"""

def Transposition(n, i, j) :
    out = Id(n)
    
    list[i] = j
    list[j] = i
    
    return out

def Cycle(n, C) :
    f = Id(n)
    
    for i in range(len(C) -1) :
        f[C[i]] = C[i+1]
    f[C[-1]] = C[0]
    
    return f

def Orbite(sigma, x) :
    O = [x]
    y = sigma[x]
    
    while y != x :
        O.append(y)
        y = sigma[y]
    
    return O

def Orbites(sigma) :
    n = len(sigma)
    
    Orb = []
    
    B = [False] * n
    
    for x in range(n) :
        if B[x] == False :
            O = Orbite(sigma, x)
            
            Orb.append(O)
            for y in O :
                B[y] = True
    
    return Orb

