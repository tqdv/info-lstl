from numpy import log as ln
from fractions import Fraction

# Exercice 1

def f(x) :
    print(x + 1)

def g(x) :
    return x + 1 


# Exercice 2

def max(a, b) :
    if a > b :
        return a
    else :
        return b

def max_3(a, b, c) :
    if a > b :
        if a > c :
            return a
        else :
            return c
    else :
        if b > c :
            return b
        else :
            return c

def max_4(a, b, c, d) :
    return max(max(a,b), max(c,d))


# Exercice 3

def quelques_uns() :
    for x in range(0, 5) :
        print(x)

def quelques_autres() :
    for x in range(0, 9, 2) :
        print(x)

def encore_un_peu() :
    for x in range(5, 0, -1) :
        print(x)

def Croissant() :
    for num in range(1, 11) :
        print(num)

def Décroissant() :
    for num in range(10, 0, -1) :
        print(num)

def odd_29to1() :
    for num in range(29, -1, -2) :
        print(num)

def Truc(y) :
    x = 1
    e = 0
    while x < y :
        x *= 2
        e += 1
    return e

def Machin(y) :
    x = 1
    e = 0
    while x < y :
        x *= 2
    e += 1
    return e

# This is an infinite loop if x < y
def Bidule(y) :
    x = 1
    e = 0
    while x < y :
        e += 1
    x *= 2
    return e

def ilogb(x, base) :
    t = 1
    e = 0
    while t <= x :
        t *= base
        e += 1
    return e-1

def llog(x, base, precision) :
    return ilogb(x**precision, base) / precision

def lim3nn(epsilon) :
    n = 0
    comparant = 1
    while comparant > epsilon :
        n += 1
        comparant *= 3 / n
    return n

def factorial(n) :
    o = 1
    for i in range(1, n+1) :
        o *= i
    return o

def Calculer_e_1(epsilon) :
    sum = 0
    for i in range(lim3nn(epsilon)) :
        sum += 1/ factorial(i)
    return sum


