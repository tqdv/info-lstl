# 2016-11-09

# Compute ch(x)

from decimal import Decimal, getcontext

getcontext().prec = 1050

def get_N(x, epsilon) :
    N = 0
    while x**(2*N+1) /fact(2*N+1) *2 *3**(ceil(x)) > epsilon :
        N += 1
    return N

def ch_N(x, epsilon) :
    N = get_N(x, epsilon)
    
    sum = 0
    i = 0
    while i <= N :
        sum += x**(2*i)/fact((2*i))
        i += 1
    
    return sum

def fact(x) :
    prod = 1
    i = 1
    while i <= x :
        prod *= i
        i += 1
    return prod

def ceil(x):
    ceil = 0
    while ceil < x :
        ceil += 1
    return ceil

def Somme_ch(x, N):
    S = Decimal(0)
    xp2n = Decimal(1)
    fac2n = Decimal(1)
    for n in range(0, N + 1):
        S += xp2n / fac2n
        xp2n *= x ** 2
        fac2n *= (2*n+1) * (2*n +2)
    return S

def ch_dec(x, epsilon):
    return Somme_ch(x, get_N(x, epsilon))


def arctan_N(x, epsilon):
    N = 1
    num = x
    denum = 1
    while num/denum > epsilon :
        num  *= x ** 2
        denum += 2
        N += 1
#        print("precision :", N)
    return N - 1


ZERO = Decimal(0)

def arctan(x, epsilon):
    i = ZERO
    upper = arctan_N(x, epsilon) - 1
    if upper < 0 :
        upper = ZERO
    print("Done setup")
    sum = ZERO
    num = Decimal(x)
    denum = Decimal(1)
    while i <= upper :
        sum += num/denum
        num *= Decimal((-1) * x**2)
        denum += Decimal(2)
        i += 1
#        print('sum @', i, ' : ', sum)
    return sum

