# 2017-01-03
from random import randint
from random import random

# Returns a random element from a list
def rand_elem(L) :
    return L[randint(0, len(L) - 1)]

# Verifies the randomness of randint
def rand_verify(n) :
    L = [0] * 10
    for i in range(n) :
        L[randint(0, 9)] += 1
    for i in range(10) :
        L[i] /= n
    print(L)

def Freq_randint(a,b, N = 1000000) :
    eff = [0] * (b - a + 1)
    for _ in range(N) :
        eff[randint(a,b) - a] += 1
    for i in range(0, b - a + 1) :
        print(str(a + i) + " : " + str(100 * eff[i] / N) + " %", sep='', end='')

# Generates random sentence
sujets = ["A", "B", "C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
verbes = ["&", "é", '"', "(", "-", "è", "_", "ç", "à", ")", "="]
complements = ["0","1","2","3","4","5","6","7","8","9"]

det_ms = ["un", "le"]
det_p = ["des", "les"]
det_fs = ["une", "la"]
nom_ms = ["chien", "chat"]
nom_mp = ["chiens", "chats"]
nom_fs = ["table", "chaise"]
nom_fp = ["tables", "chaises"]
adj_ms = ["rouge", "bleu"]
adj_mp = ["rouges", "bleus"]
adj_fs = ["rouge", "bleue"]
adj_fp = ["rouges", "bleues"]
ver_s = ["est", "mange"]
ver_p = ["sont", "mangent"]

det = [[det_ms, det_p], [det_fs, det_p]]
nom = [[nom_ms, nom_mp], [nom_fs, nom_fp]]
adj = [[adj_ms, adj_mp], [adj_fs, adj_fp]]
ver = [ver_s, ver_p]

def gen():
    s = gen_s()
    v = rand_elem(verbes)
    c = rand_elem(complements)
    print(Majusculiser(s + " " + v + " " + c))

def gen_s():
    genre = randint(0,1)
    nombre = randint(0,1)
    
    d = rand_elem(det[genre][nombre])
    n = rand_elem(nom[genre][nombre])
    a = ""
    if Bernoulli(0.2) :
        a = " " + rand_elem(adj[genre][nombre])
    
    gn = d + " " + n + a
    v = rand_elem(ver[nombre])
    o = gen_gn()
    return gn + " " + v + " " + o + "."

def gen_gn() :
    genre = randint(0,1)
    nombre = randint(0,1)
    
    d = rand_elem(det[genre][nombre])
    n = rand_elem(nom[genre][nombre])
    a = ""
    b = ""
    if Bernoulli(0.03) :
        a = " " + rand_elem(adj[genre][nombre])
    if Bernoulli(0.45) :
        b = " " + rand_elem(adj[genre][nombre])
    
    return d + a + " " + n + b

def Majusculiser(s):
    return s[0].upper() + s[1:]

def Bernoulli(p) :
    U = random()
    return U < p

def CommenceParVoyelle(s):
    return s[0] in ["a", "e", "i", "o", "u", "y"]

# From StackOverflow
def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        for p in permute(xs, low + 1):
            yield p        
        for i in range(low + 1, len(xs)):        
            xs[low], xs[i] = xs[i], xs[low]
            for p in permute(xs, low + 1):
                yield p        
            xs[low], xs[i] = xs[i], xs[low]





































# gen all lists of length `n` with values of indexes.
# then remove doubles