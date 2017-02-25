# pdm 1 d'info

def Distribuer(x, P):
    for list_ in P :
        if x not in list_ :
            P.append(list_ + [x])
    return P

def Parties_1(L):
    P = [[]]
    for elem in L :
        P = Distribuer(elem, P)
    return P

def Binaire(x,r):
    L = []
    for i in range(r) :
        L.append(x % 2)
        x //= 2
    return L

def Partie(L, chi):
    out = []
    for i in range(len(chi)) :
        if chi[i] == 1 :
            out.append(L[i])
    return out
def Parties_2(L):
    P = []
    for i in range(2**len(L)) :
        P.append(Partie(L,Binaire(i, len(L))))
    return P

print(Parties_1(list(range(5))))
print(Parties_2(list(range(5))))
