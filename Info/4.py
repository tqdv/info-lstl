from numpy import sqrt

def square(x) :
    comp = 1
    somme = 1

    while somme < x :
        comp += 2
        somme += comp
        if x == somme :
            return True
    return False

def intsqrt(x) :
    count = 0
    incr = 1
    comp = 1

    while comp <= x :
        count += 1
        incr += 2
        comp += incr
    return count 

def pgfc(x):
    k = intsqrt(x)
    while k>= 1 and n % (k**2) != 0 :
        k -= 1
    return (k, n// (k**2))

def sr(x):
    (k, d) = pgfc(x)
    return "sqrt(" + str(x) + ") = " + str(k) + " x sqrt(" + str(d) + ")"

def compprod(k1,d1,k2,d2):
    if k1 < 0 and k2 >= 0 :
        return True
    elif k1 >= 0 and k2 < 0 :
        return False
    elif k1 >= 0 and k2 >= 0 :
        return k1**2 *d1 <= k2**2 *d2
    else :
        return k1**2 *d1 >= k2**2 *d2


def f(x):
    return (2*x + 3