from time import clock

# Actual Sum
def SommePartielle (L, a, b) :
    s = 0
    for i in range (a, b+1) :
        s += L[i]
    return s

# Partial Sum
def SommesPartielles_1 (L) :
    S = []
    for i in range (0, len(L)) :
        S.append ( SommePartielle (L, 0, i) )
    return S

# Partial Sum
def SommesPartielles_2 (L) :
    S = [0] * len(L)
    S[0] = L[0]
    for i in range (1, len(L)) :
        S[i] = S[i -1] + L[i]
    return S

# Timer for previous functions
def Chrono ( Programme , L) :
    deb = clock ()
    _ = Programme (L)
    fin = clock ()
    return fin - deb
    
# 1 : 1.0202895396105305e-05
# 2 : 4.328501063355361e-06
#
# tmw when you write in YAML

from random import randint

def ListeAleatoire (n) :
    L = []
    for _ in range (n) :
        L.append (randint ( -100 , 100))
    return L

from matplotlib.pyplot import scatter , grid , show , close

def VisualiserTemps ( Programme ) :
    Tailles = [ 50 * 2**i for i in range (0, 6+1) ]
    Temps = [ Chrono ( Programme , ListeAleatoire (n)) for n in Tailles ]
    grid ( True )
    scatter ( Tailles , Temps )
    show ()

from numpy import log as ln , polyfit

def ModeliserTemps ( Programme ) :
    Tailles = [ 50 * 2**i for i in range (0, 6+1) ]
    Temps = [ Chrono ( Programme , ListeAleatoire (n)) for n in Tailles ]
    lnTailles = [ ln(n) for n in Tailles ]
    lnTemps = [ ln(t) for t in Temps ]
    grid ( True )
    scatter ( lnTailles , lnTemps )
    show ()
    return polyfit ( lnTailles , lnTemps , 1)
# polyfit is the linear regression

def Minimum(L):
    min = L[0]
    for element in range(1,len(L)):
        if L[element] < min :
            min = L[element]
    return min

def IndiceMinumum(L):
    min = L[0]
    indice = 0
    for element in range(0,len(L)):
        if L[element] < min :
            min = L[element]
            indice = element
    return indice

def MinimumSousListe(L, a, b):
    min = L[a]
    for element in range(a, b + 1):
        if L[element] < min :
            min = L[element]
    return min

def IndiceMinimumSousListe(L, a, b):
    min = L[a]
    indice = a
    for element in range(a, b+1):
        if L[element] < min :
            min = L[element]
            indice = element
    return indice

# Selection Sort
def sort(L):
    last = len(L) - 1
    for i in range(len(L)):
        index = IndiceMinimumSousListe(L, i, last)
        temp = L[i]
        L[i] = L[index]
        L[index] = temp
    return L

def bigC(Programme):
    Tailles = [ 50 * 2**i for i in range (0, 6+1) ]
    Temps = [ Chrono ( Programme , ListeAleatoire (n)) for n in Tailles ]
    lnTailles = [ ln(n) for n in Tailles ]
    lnTemps = [ ln(t) for t in Temps ]
    grid ( True )
    scatter ( Tailles , Temps )
    show ()
    return polyfit ( lnTailles , lnTemps , 1)

def MaximumSousListe(L, a, b):
    max = L[a]
    for element in range(a, b + 1):
        if L[element] > max :
            max = L[element]
    return min

def IndiceMaximumSousListe(L, a, b):
    max = L[a]
    indice = a
    for element in range(a, b+1):
        if L[element] > max :
            max = L[element]
            indice = element
    return indice

def MaxIndexSublist(L, a, b):
    return IndiceMinimumSousListe(L, a, b), IndiceMaximumSousListe(L, a, b)

def swap (L, a, b) :
    temp = L[a]
    L[a] = L[b]
    L[b] = temp

def sortagain(L):
    last = len(L) - 1
    for i in range(len(L) // 2):
        (min, max) = MaxIndexSublist(L, i, last - i)
        swap(L, i, min)
        swap(L, last - i, max)
    return L

def Maximum(L):
    max = L[0]
    for element in range(len(L)):
        if L[element] > max :
            max = L[element]
    return max

def Extr(L):
    return Minimum(L), Maximum(L)

def Effect(L):
    min, max = Extr(L)
    E = []
    for i in range(min, max + 1):
        count = 0
        for elem in L:
            if i == elem :
                count += 1
        E.append(count)
    return E

def strangestuff(E, m):
    K = []
    for i in range(len(E)):
        K += [m+i] * E[i]
    return K