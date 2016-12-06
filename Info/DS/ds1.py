# Correction du DS N°1


## Exercice 1

def Seuil(s, ε):
    N = 1
    s = s - 1
    while 1 / (s * N**s) > ε :
        N += 1
    return N

def zeta(s, ε):
    index = 1
    somme = 0
    N = Seuil(s, ε)
    while index <= N :
        somme += 1 / (index**s)
        index += 1
    return somme

def Dichotomie(f, a, b, ε):
    c = (a + b)/ 2
    while b - a > ε :
        if f(a) * f(c) <= 0 :
            b = c
        else :
            a = c
        c = (a + b) / 2
    return c

def BorneGauche(y, ε):
    x = 2
    while zeta(x, ε) < y :
        x = (x - 1) / 2 + 1
    return x

def BorneDroite(y, ε):
    x = 2
    while zeta(x, ε) > y :
        x += 1
    return x

def Réciproque(y, ε):
    def f(x):
        return zeta(x, ε) - y
    return Dichotomie(f, BorneGauche(y, ε), BorneDroite(y, ε),ε)


print(Réciproque(2, 1e-3))


## Exercice 2

from matplotlib.pyplot import plot, show, grid
from numpy import linspace

def Intervalle(f, u_0, n_max):
    x_min = 0
    x_max = 0
    n = 0
    u_n = u_0
    while n <= n_max :
        if u_n < x_min :
            x_min = u_n
        elif u_n > x_max :
            x_max = u_n
        
        u_n = f(u_n)
        n += 1
    return (x_min, x_max)

def DessinerToile(f, u_0, n_max):
    u = f(u_0)
    X = [u_0, u_0]
    Y = [0, u]
    n = 1
    while n <= n_max :
        X += [u] * 2
        Y.append(u)
        u = f(u)
        Y.append(u)
        n += 1
    plot(X,Y, color='red')
    return 0

def ReprésenterSuite(f, u_0, n_max):
    (x_min, x_max) = Intervalle(f, u_0, n_max)
    Id = [x_min, x_max]
    plot(Id, Id, color='grey')
    X = linspace(x_min, x_max, 100000)
    Y = [f(x) for x in X]
    plot(X, Y, color='purple')
    DessinerToile(f, u_0, n_max)
    grid(True)
    show()
    return 0

import math

def f(x):
    return 2 * math.sqrt(x)


ReprésenterSuite(f, 10, 20)


## Exercice 3

def EstSansFacteurCarré(x):
    k = 1
    p = 1
    while p <= x :
        if p == x :
            return False
        k += 1
        p = k * k
    return True

def add(x, y):
    (ax, bx) = x
    (ay, by) = y
    return (ax + ay, bx + by)

def sstr(x, y):
    (ax, bx) = x
    (ay, by) = y
    return (ax - ay, bx - by)

def mul(x, y):
    global d
    (ax, bx) = x
    (ay, by) = y
    return (ax*ay + d*bx*by, ax*by + ay*bx)

from fractions import Fraction

def div(x, y):
    global d
    (ay, by) = y
    (ap, bp) = mul(x, (ay, -by))
    denom = ay**2 - by**2 * d
    return (Fraction(ap, denom), Fraction(bp, denom))

def PlusGrandCarréInférieur(x):
    n = 1
    while n * n <= x :
        n += 1
    return n - 1

def PartieEntière(a,b):
    global d
    alpha = PlusGrandCarréInférieur(b**2 * d)
    sum = a + alpha
    # Don't even ask why this works
    if b**2 >= (1 + alpha - a % 1 )**2 / d :
        sum += 1
    return sum.numerator // sum.denominator

def DFC(a, b, n):
    x = PartieEntière(a, b)
    r = (a - x, b)
    print('[', x, '; ', sep='', end='')
    k = 1
    while k <= n :
        q = div((1, 0), r)
        (a, b) = q
        x = PartieEntière(a, b)
        r = sstr(div((1, 0), r), (x, 0))
        print(x, ', ', sep='', end='')
        k += 1
    print('...]')
    return 0


d = 2
DFC(5,134,28)