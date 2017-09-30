#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Compression BZIP
# D'après X - MP/PC 2007


def Occurences(T, n) :
    E = [] * 256 # Effectif

    for i in T :
        E[i] += 1

    return E


def OccurencesPartielles(T, déb, fin) :
    E = [] * 256

    for i in range(déb, fin +1) :
        E[T[i]] += 1

    return E


def PremierPlusRare(T,n) :
    E = Occurences(T, n)

    index = 0 ; minimum = T[0]
    for i in range(len(T)) :
        current = E[i]

        if current < minimum :
            minimum = current
            index = i

    return index

# On suppose que le marqueur n'apparaît pas dans le texte
def TailleCodage(T, n) :
    i = 0 ; taille = 1
    while i < len(T) :
        if i+1 < len(T) and T[i] == T[i+1] : # Il reste au moins 2 éléments
            taille += 3
            caractère = T[i]

            while T[i] == caractère :
                    i += 1

        else :
            taille += 1
            i += 1

    return taille


def Codage(T, n) :
    marqueur = PremierPlusRare(T, n)

    i = 0 ; T_ = [marqueur]
    while i < len(T):
        if i+1 < len(T) and T[i] == T[i+1]:  # Il reste au moins 2 éléments
            déb = i
            caractère = T[i]

            while T[i] == caractère:
                i += 1

            T_ += [marqueur, caractère, i - déb -1]

        else :
            T_.append(T[i])

    return T_


def ComparerRotation(T, n, i, j) :
    for char in range(n) :
        if T[i] > T[j] :
            return 1
        elif T[i] < T[j] :
            return -1
        else :
            i = (i+1) % n
            j = (j+1) % n

    return 0


def triRotations(T, n) :
    Ind = list(range(n))

    def rotate(p):
        return T[p:] + T[:p]

    Ind.sort(rotate)

    return Ind


def CodageBW(T, n) :
    Ind = triRotations(T, n)
    Code = []
    indice = -1

    lettre = T[0]
    trouvée = False

    for i in range(n) :
        courant = T[(Ind[i] -1) % n]
        Code.append(courant)

        if not trouvée and courant == lettre :
            indice = i

    Code.append(indice)

    return Code


def TrierCars(T_, n_) :
    E = OccurencesPartielles(T_, 0, n_ -1)

    TriCars = []

    for i in range(256) :
        TriCars += [i] * E[i]

    return TriCars


def TrouverIndices(T_, n_) :
    Indices = []
    TriCars = TrierCars(T_, n_)

    i = 0
    while i < n_ -1 :
        courant = TriCars[i]

        for indice in range(n_ -1) :
            if T_[indice] == courant :
                Indices.append(indice)

        while TriCars[i] == courant :
            i += 1

    return Indices


def DécodageBW(T_, n_) :
    Indices = TrouverIndices(T_, n_)
    clé = T_[-1]

    T = [T_[clé]]

    courant = Indices[clé]

    while courant != clé :
        T.append(T_[courant])

        courant = Indices[courant]

    return T