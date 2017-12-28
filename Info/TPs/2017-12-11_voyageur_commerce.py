# -*- coding: UTF-8 -*-

# TP : Problème du voyageur de commerce (dans le plan)

# Naif_1 : chemin aléatoire
# Naif_2 : tous les chemins
# Glouton_1 : point le plus proche du dernier
#   Glouton_1_1 : Glouton_1 pas à pas
#   Glouton_1_2 : Glouton_1 à partir de chaque point
# Glouton_2 : insérer dans le segment qui minimise le poids
#             (points dans l'ordre)
#   Glouton_2_1 : Glouton_2 pas à pas
#   Glouton_2_2 : Glouton_2 pour chaque point
#   Glouton_2_2_1 : Glouton_2_2 pas à pas (pause de 0.5 s)
#   Glouton_2_3 : Glouton_2_2 à partir de chaque point
#
# test1 : aléatoire avec 10 points
# test2 : aléatoire avec 10 points et affiche le graphe
# test3 : Naif_1 avec 10 points et 100.000 essais
# test4 : débogage de Naif_2
# test5 : compare Naif_1 et Naif_2
# test6 : Glouton_1 avec 30 points
# test7 : Glouton_1_1 avec 80 points
# test8 : Glouton_1_2 avec 40 points
# test9 : Glouton_2 avec 50 points
# test10 : Glouton_2_1 avec 50 points
# test11 : Glouton_2_2 avec 30 points
# test12 : Glouton_2_2_1 avec 30 points
# test13 : Glouton_2_3 avec 30 points

# J'ai passé tellement de temps sur ces fonctions que je pense qu'il est
# judicieux que je les mette en valeur :
# - PermutationSuivante_1
# - CombiSuivant_1


from random import random, shuffle, randint
from numpy import log as ln, ceil
from math import factorial, sqrt
from matplotlib import use

use("TkAgg")

from matplotlib.pyplot import (
    plot, scatter, show, close, interactive, isinteractive, clf, draw, pause
)

interactive(True)  # Automatic if backend is interactive


def Nuage(N):
    X = [random() for _ in range(N)]
    Y = [random() for _ in range(N)]
    return X, Y


# Déplace le barycentre en 0, puis on divise par le maximum des normes
# Préserve les rapports de distance

# C : liste de sommets qui représente un chemin
def DessinerChemin(X, Y, C):
    XC = [X[c] for c in C]
    YC = [Y[c] for c in C]

    # Dessin du chemin
    plot(XC, YC, color=[0.5, 0, 0.75])
    # Dessin du nuage
    scatter(X, Y, color=[0.7, 0.2, 0.9])
    show()


def CH_aleatoire(N):
    L = list(range(N))
    shuffle(L)
    L.append(L[0])
    return L


def test1():
    (X, Y) = Nuage(10)
    C = CH_aleatoire(10)
    G = mat_adjacence(X, Y)
    return Poids(G, C)


def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mat_adjacence(X, Y):
    n = len(X)
    return [[distance(X[i], Y[i], X[j], Y[j]) for j in range(n)]
            for i in range(n)]


def Poids(G, C):
    p = 0
    for i in range(len(C) - 1):
        p += G[C[i]][C[i + 1]]
    return p


def test2():
    (X, Y) = Nuage(10)
    C = CH_aleatoire(10)
    DessinerChemin(X, Y, C)
    G = mat_adjacence(X, Y)
    return Poids(G, C)


def Naif_1(X, Y, NB_ESSAIS=100):
    if not NB_ESSAIS > 0:
        return

    n = len(X)
    G = mat_adjacence(X, Y)
    C = minC = CH_aleatoire(n)
    p = minp = Poids(G, C)

    for i in range(NB_ESSAIS - 1):
        C = CH_aleatoire(n)
        p = Poids(G, C)
        if p < minp:
            minp = p
            minC = C
    DessinerChemin(X, Y, minC)
    return minp


def test3():
    X, Y = Nuage(10)
    print(Naif_1(X, Y, 100000))


# Aparté sur la probabilité que l'algorithme Naif_1 trouve la solution optimale


def proba(N):
    return 2 / factorial(N - 1)


# nb essais pour trouver optimal pour à alpha% erreur pour N sommets
def Trouver_K(N, alpha):
    return int(ceil(ln(1 - alpha) / ln(1 - proba(N))))


# Fin de l'aparté

def UpletSuivant(L):
    n = len(L)
    i = len(L) - 1
    while i >= 0:
        if L[i] < n - 1:
            L[i] += 1
            return L
        else:
            L[i] = 0
            i -= 1
    return None


def EstPermutation(L):
    vu = [False for _ in range(len(L))]
    for i in L:
        vu[i] = True
    for i in vu:
        if not i:
            return False
    return True


def PermutationSuivante(L):
    N = UpletSuivant(L)
    if N is None:
        return None
    while not EstPermutation(N):
        N = UpletSuivant(N)
        if N is None:
            return None
    return N


def PermutationSuivante_1(L):
    n = len(L)
    if not n > 0:
        return None

    # NB : copier-coller de CombiSuivant_1 avec lt -> n et T -> L
    #      PermutationSuivante_1 est un cas particulier de CombiSuivant_1
    #      avec `len(T) == n`
    # NB : pos peut être une liste de booléens (?)
    # Vérifie que L soit une combinaison, et dans le cas contraire,
    # modifie L pour qu'elle le soit. Construit aussi `pos`
    # pos : Position de l'élément dans la combinaison
    pos = [None] * n
    i = 0
    correct = True
    while i < n and correct:
        if not L[i] < n:
            return None
        if L[i] < 0:
            L[i] = 0
            correct = False
        elif pos[L[i]] is None:
            pos[L[i]] = i
            i += 1
        else:
            # 0 <= L[i] < n and pos[L[i]] != None
            correct = False

    if not correct:
        # `i_erreur` indice de la première erreur
        i_erreur = i
        val_erreur = L[i_erreur]
        trouve = False
        while not i < 0 and not trouve:
            # Cherche une valeur supérieure
            cur_val = L[i]
            j = cur_val + 1
            if cur_val < 0:
                j = 0

            while j < n and pos[j] is not None:
                j += 1
            if j == n:
                # Pas trouvé, on libère la place et on passe au suivant
                # Sauf si c'est `i_erreur`, car sa valeur a déjà été rencontrée
                # T/S : si le code casse, vérifier ici
                if i != i_erreur:
                    pos[cur_val] = None
                i -= 1
            else:
                nv_val = j
                L[i] = j
                pos[nv_val] = i
                # T/S : je ne sais pas pourquoi
                if not cur_val < 0 and i != i_erreur:
                    pos[cur_val] = None
                trouve = True

        if i < 0:
            # Pas moyen d'avoir une combinaison correcte (?)
            return None

        # Complète les éléments suivants de L (dans l'ordre croissant)
        i += 1
        j = 0  # Parcoure `pos`, c'est la valeur de l'élément
        while i < n:
            while j < n and pos[j] is not None:
                j += 1
            if j == n:
                raise Exception("Impossible (?), cf code")
                # Pas assez d'éléments disponibles dans pos (plus de n élts)
                # C'est impossible (?)
            L[i] = j
            # pos[j] = i
            j += 1
            i += 1
        return L
    # NB : Fin du copier-coller

    # On cherche la plus longue suite décroissante en partant de la fin
    i = n - 2  # i indice de l'élément avant la suite décroissante
    trouve = False
    while not i < 0 and not trouve:
        if not L[i] > L[i+1]:
            trouve = True
        else:
            i -= 1
    if i < 0:
        return None

    # On remet les éléments dans l'ordre
    # i _ k -> <- j _ n
    j = n - 1
    k = i + 1
    while j > k:
        L[k], L[j] = L[j], L[k]
        j -= 1
        k += 1

    # Place L[i] à sa nouvelle place
    j = i + 1
    while L[j] < L[i]:
        j += 1
    if j == n:
        raise Exception("Pas d'élément supérieur dans le reste !?")
    L[i], L[j] = L[j], L[i]

    return L


def Naif_2(X, Y):
    P = [0 for _ in range(len(X))]
    C = C_min = P + [P[0]]
    if not EstPermutation(P):
        P = PermutationSuivante(P)
        C = C_min = P + [P[0]]
    G = mat_adjacence(X, Y)
    p = p_min = Poids(G, C)
    P = PermutationSuivante(P)
    while P is not None:
        C = P + [P[0]]
        p = Poids(G, C)
        if p < p_min:
            p_min = p
            C_min = C
        P = PermutationSuivante(P)
    DessinerChemin(X, Y, C_min)
    return p_min


# Je saute `EsperancepoidsMinimal(N)`


def PlusProcheParmi(G, x, V):
    if not len(V) > 0:
        return
    n = len(V)
    P = min_P = V[0]
    d = min_d = G[x][P]
    for i in range(1, n):
        P = V[i]
        d = G[x][P]
        if d < min_d:
            min_P = P
            min_d = d
    return min_P


def test4():
    X = [0, 0, 1]
    Y = [0, 1, 0]
    print "poids min :", Naif_1(X, Y)
    clf()
    return Naif_2(X, Y)


def test5():
    X, Y = Nuage(7)
    p1 = Naif_1(X, Y)
    print "1:", p1
    p2 = Naif_2(X, Y)
    print "2:", p2


# Pour ne pas utiliser list.remove()
def retirer_elem(L, x):
    n = len(L)
    i = 0
    while i < n and L[i] != x:
        i += 1
    if i == n:
        raise Exception("Élément absent de la liste")
    L = L[:i] + L[i + 1:]
    return L


# Et si je veux modifier sur place ?
# Ceci est probablement horrible niveau complexité
def retirer_elem_en_place(L, x):
    n = len(L)
    i = 0
    while i < n and L[i] != x:
        i += 1
    if i == n:
        raise Exception("Élément absent de la liste")
    while i + 1 < n:
        L[i], L[i + 1] = L[i + 1], L[i]
        i += 1
    L.pop()


# Crée un circuit en prenant le point le plus proche du dernier
def Glouton_1(X, Y):
    n = len(X)
    p = randint(0, n - 1)
    G = mat_adjacence(X, Y)
    C = [p]
    V = list(range(n))
    V.remove(p)
    while V:
        p = PlusProcheParmi(G, p, V)
        C.append(p)
        V.remove(p)
    C.append(C[0])
    DessinerChemin(X, Y, C)
    G = mat_adjacence(X, Y)
    return Poids(G, C)


# On modifie pour pouvoir voir le tracé étape par étape
def DessinerChemin_1(X, Y, C):
    XC = [X[c] for c in C]
    YC = [Y[c] for c in C]

    clf()
    # Dessin du chemin
    plot(XC, YC, color=[0.5, 0, 0.75])
    # Dessin du nuage
    scatter(X, Y, color=[0.7, 0.2, 0.9])
    draw()


def Glouton_1_1(X, Y):
    n = len(X)
    p = randint(0, n - 1)
    G = mat_adjacence(X, Y)
    C = [p]
    V = list(range(n))
    V.remove(p)
    DessinerChemin_1(X, Y, C)
    show()
    while V:
        p = PlusProcheParmi(G, p, V)
        C.append(p)
        V.remove(p)
        DessinerChemin_1(X, Y, C)
    C.append(C[0])
    DessinerChemin(X, Y, C)
    G = mat_adjacence(X, Y)
    return Poids(G, C)


def test6():
    X, Y = Nuage(30)
    return Glouton_1(X, Y)


def test7():
    X, Y = Nuage(80)
    return Glouton_1_1(X, Y)


# On n'obtient pas toujours le même circuit lorsque l'on part de sommets
# différents


# Même chose, mais cette fois-ci, on teste tous les points de départ
def Glouton_1_2(X, Y):
    # o = origine
    # p = poids
    n = len(X)
    if not n:
        raise Exception("Pas de points")
    G = mat_adjacence(X, Y)
    o_min = 0

    def aux(o):
        P = 0
        C = [o]
        V = list(range(n))
        V.remove(o)
        p = o
        while V:
            p1 = PlusProcheParmi(G, p, V)
            C.append(p1)
            V.remove(p1)
            P += G[p][p1]
            p = p1
        C.append(o)
        P += G[p][o]
        return C, P

    C_min, P_min = aux(o_min)

    for i in range(1, n):
        C, P = aux(i)
        if P < P_min:
            C_min = C
            o_min = i
            P_min = P

    DessinerChemin(X, Y, C_min)
    return o_min, P_min


def test8():
    X, Y = Nuage(40)
    return Glouton_1_2(X, Y)


# Si list.insert(i, x) n'est pas autorisé
def InsererDansListe(L, i, x):
    return L[:i] + [x] + L[i:]


# Et sur place (avec list.pop() et list.append())
def InsererDansListe_1(L, i, x):
    n = len(L) - 1 - i
    R = []
    for j in range(n):
        if L:
            R.append(L.pop())
    L.append(x)
    while R:
        L.append(R.pop())


# Sur place encore
def InsererDansListe_2(L, i, x):
    n = len(L)
    t = x
    if i < -n:
        i = 0
    elif -n <= i < 0:
        i = n + i

    for i in range(i, n):
        L[i], t = t, L[i]
    L.append(t)


# C est un circuit
def InsererAuMieux(G, x, C):
    n = len(C)
    if n == 0:
        C.append(x)
        return
    if n == 1:
        C.append(x)
        C.append()
        return

    p_min = G[C[0]][x] + G[x][C[1]]
    # i_min est l'indice d'insertion
    # i est l'indice de test (càd "i_min" - 1)
    i_min = 1
    i = 1
    while i + 1 < n:
        p = G[C[i]][x] + G[x][C[i + 1]]
        if p < p_min:
            p_min = p
            i_min = i + 1
        i += 1

    C.insert(i_min, x)


# Si list.pop(i) n'est pas autorisé
# Ne sera pas corrigé :
#     >>> L = list(range(10))
#     >>> RetirerParIndice(L, -1)
#     [0, 1, 2, 3, 4, 5, 6, 7, 8, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def RetirerParIndice(L, i):
    return L[:i] + L[i + 1:]


# Et sur place (avec list.pop() et list.append())
# Cette implémentation ne prend pas en charge l'accès par indices négatifs
def RetirerParIndice_1(L, i):
    n = len(L) - 1 - i
    if n < 0:
        return
    R = []
    for i in range(n):
        if L:
            R.append(L.pop())
    if L:
        L.pop()
    while R:
        L.append(R.pop())


def RetirerParIndice_2(L, i):
    n = len(L)
    if i < -n:
        i = 0
    elif -n <= i < 0:
        i += n

    for j in range(i, n - 1):
        L[j] = L[j + 1]
    L.pop()


def Glouton_2(X, Y):
    n = len(X)
    if n < 3:
        return
    C = []
    R = list(range(n))
    for i in range(3):
        p = randint(0, n - 1 - i)
        C.append(R[p])
        R.pop(p)  # ou `del R[p]`
    C.append(C[0])

    G = mat_adjacence(X, Y)
    for x in R:
        InsererAuMieux(G, x, C)

    DessinerChemin(X, Y, C)
    return Poids(G, C)


def test9():
    X, Y = Nuage(50)
    return Glouton_2(X, Y)


# Et avec animation !
def Glouton_2_1(X, Y):
    n = len(X)
    if n < 3:
        return
    C = []
    R = list(range(n))
    for i in range(3):
        p = randint(0, n - 1 - i)
        C.append(R[p])
        R.pop(p)  # ou `del R[p]`
    C.append(C[0])

    DessinerChemin_1(X, Y, C)
    show()

    G = mat_adjacence(X, Y)
    for x in R:
        InsererAuMieux(G, x, C)
        DessinerChemin_1(X, Y, C)
    return Poids(G, C)


def test10():
    X, Y = Nuage(50)
    return Glouton_2_1(X, Y)


# Retourne un indice d'insertion et un poids
def InsererAuMieux_2(G, x, C):
    n = len(C)
    if n == 0:
        C.append(x)
        return
    if n == 1:
        C.append(x)
        C.append()
        return

    p_min = G[C[0]][x] + G[x][C[1]]
    # i_min est l'indice d'insertion
    # i est l'indice de test (càd "i_min" - 1)
    i_min = 1
    i = 1
    while i + 1 < n:
        p = G[C[i]][x] + G[x][C[i + 1]]
        if p < p_min:
            p_min = p
            i_min = i + 1
        i += 1

    return i_min, p_min


# Et si on veut une figure (à peu près) convexe ?
# Prendre le point le plus proche du circuit et l'insérer
def Glouton_2_2(X, Y):
    n = len(X)
    if n < 3:
        return
    C = []
    R = list(range(n))
    for i in range(3):
        p = randint(0, n - 1 - i)
        C.append(R[p])
        R.pop(p)
    C.append(C[0])

    G = mat_adjacence(X, Y)

    while R:
        nb_reste = len(R)
        insertion_min, poids_min = InsererAuMieux_2(G, R[0], C)
        x_min = R[0]
        i_min = 0
        for i in range(1, nb_reste):
            insertion_x, poids_x = InsererAuMieux_2(G, R[i], C)
            if poids_x < poids_min:
                insertion_min = insertion_x
                poids_min = poids_x
                x_min = R[i]
                i_min = i
        C.insert(insertion_min, x_min)
        R.pop(i_min)

    DessinerChemin(X, Y, C)
    return Poids(G, C), C


def test11():
    X, Y = Nuage(30)
    return Glouton_2_2(X, Y)


# Et avec animation ! Encore !
def Glouton_2_2_1(X, Y):
    n = len(X)
    if n < 3:
        return
    C = []
    R = list(range(n))
    for i in range(3):
        p = randint(0, n - 1 - i)
        C.append(R[p])
        R.pop(p)
    C.append(C[0])

    DessinerChemin_1(X, Y, C)
    show()
    pause(0.5)

    G = mat_adjacence(X, Y)
    while R:
        nb_reste = len(R)
        insertion_min, poids_min = InsererAuMieux_2(G, R[0], C)
        x_min = R[0]
        i_min = 0
        for i in range(1, nb_reste):
            insertion_x, poids_x = InsererAuMieux_2(G, R[i], C)
            if poids_x < poids_min:
                insertion_min = insertion_x
                poids_min = poids_x
                x_min = R[i]
                i_min = i
        C.insert(insertion_min, x_min)

        DessinerChemin_1(X, Y, C)
        pause(0.5)

        R.pop(i_min)
    return Poids(G, C)


def test12():
    X, Y = Nuage(30)
    return Glouton_2_2_1(X, Y)


# Ici, on ne vérifie seulement la croissance car c'est un triangle
# ... si ce n'était pas une fonction générique
def EstCombi(T, n):
    vu = [False] * n
    for i in T:
        if not vu[i]:
            vu[i] = True
        else:
            return False
    return True


def CombiSuivant(T, n):
    def TripletSuivant(T, n):
        l = len(T)
        T[l-1] += 1
        i = l - 1
        while not i < 0 and not T[i] < n:
            T[i] %= n
            i -= 1
            T[i] += 1
        if i < 0:
            return None
        return T

    T = TripletSuivant(T, n)
    if T is None:
        return None

    while not EstCombi(T, n):
        T = TripletSuivant(T, n)
        if T is None:
            return None
    return T


def CombiSuivant_1(T, n):
    lt = len(T)
    if not lt > 0:
        return None

    # Vérifie si T est une combinaison, et dans le cas contraire, renvoie
    # l'indice de la première erreur. Remplit aussi partiellement `pos`
    def EstCombiErreur(T, pos):
        lt = len(T)
        n = len(pos)
        i = 0
        i_erreur = None
        while i < lt and i_erreur is None:
            if not T[i] < n:
                i_erreur = i
            elif T[i] < 0:
                i_erreur = i
            elif pos[T[i]] is not None:
                i_erreur = i
            else:
                pos[T[i]] = i
                i += 1
        return i_erreur

    def ComplSuiv(T, pos, i_correct):
        # Complète les éléments suivants de T (dans l'ordre croissant)
        i = i_correct + 1
        j = 0  # Parcoure `pos`, c'est la valeur de l'élément
        while i < lt:
            while j < n and pos[j] is not None:
                j += 1
            if j == n:
                raise Exception("Impossible (?), cf code")
                # Pas assez d'éléments disponibles dans pos (plus de n élts)
                # C'est impossible (?)
            T[i] = j
            # pos[j] = i
            j += 1
            i += 1
        return T

    # Prend `pos` et `i_erreur` initialisés par `EstCombiErreur` et renvoie
    # la combinaison (strictement, car `i_erreur`) supérieure
    def CombiSup(T, pos, i_erreur):
        n = len(pos)
        lt = len(T)
        # On cherche à valider le début de la combinaison :
        # on parcoure T de i_erreur vers 0
        i = i_erreur
        trouve = False
        while i >= 0 and not trouve:
            # Cherche une valeur supérieure
            # L'élément considéré n'a pas de valeur dans `pos`
            cur_val = T[i]
            if cur_val >= n:
                i -= 1
                if i >= 0:
                    pos[T[i]] = None
            elif cur_val < -1:
                # Car on cherche toujours une valeur strictement supérieure
                T[i] = -1
            else:
                # WIP : Do you always look up ?
                j = cur_val + 1
                while j < n and pos[j] is not None:
                    j += 1
                if j == n:
                    # Pas trouvé, on passe au suivant
                    i -= 1
                    # L'élément considéré ne doit pas avoir de position !
                    if i >= 0:
                        pos[T[i]] = None
                else:
                    nv_val = j
                    T[i] = j
                    pos[nv_val] = i
                    trouve = True

        if i < 0:
            # Pas moyen d'avoir une combinaison correcte
            return None
        i_correct = i
        return ComplSuiv(T, pos, i_correct)

    # NB : `pos` peut être une liste de booléens (?)
    # pos : Position de l'élément dans la combinaison
    pos = [None] * n
    # On cherche le suivant
    T[-1] += 1
    i_erreur = EstCombiErreur(T, pos)

    print i_erreur  # DEBUG

    if i_erreur is None:  # T (modifié est une combinaison)
        return T
    else:  # i_erreur == 1..n-1
        return CombiSup(T, pos, i_erreur)


def Glouton_2_3(X, Y):
    def Glouton_2_2_alt(X, Y, C):
        n = len(C)
        if n < 3:
            return
        R = list(range(len(X)))
        for i in range(3):
            R.remove(C[i])

        G = mat_adjacence(X, Y)
        while R:
            nb_reste = len(R)
            insertion_min, poids_min = InsererAuMieux_2(G, R[0], C)
            x_min = R[0]
            i_min = 0
            for i in range(1, nb_reste):
                insertion_x, poids_x = InsererAuMieux_2(G, R[i], C)
                if poids_x < poids_min:
                    insertion_min = insertion_x
                    poids_min = poids_x
                    x_min = R[i]
                    i_min = i
            C.insert(insertion_min, x_min)
            R.pop(i_min)

        DessinerChemin(X, Y, C)
        return Poids(G, C), C

    T = [0] * 3
    if not EstCombi(T, 3):
        T = CombiSuivant(T, 3)
        if T is None:
            # Pas de combinaison !?
            return None
    T_min = list(T)
    poids_min, C_min = Glouton_2_2_alt(X, Y, list(T))
    T = CombiSuivant(T, 3)
    while T is not None:
        poids_i, C_i = Glouton_2_2_alt(X, Y, list(T))
        if poids_i < poids_min:
            poids_min = poids_i
            C_min = C_i
            T_min = list(T)
        T = CombiSuivant(T, 3)
    DessinerChemin(X, Y, C_min)
    return T_min, poids_min, C_min


def test13():
    X, Y = Nuage(30)
    return Glouton_2_3(X, Y)
