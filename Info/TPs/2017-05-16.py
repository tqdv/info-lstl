# Mastermind

# PARAMETRES DU JEU
NB_PIONS = 5
NB_COULEURS = 10

def arbitre(CS, E) :
    Bon = 0 ; Mal = 0
    CSm = [] ; Em = []
    
    for i in range(NB_PIONS) :
        if CS[i] == E[i] :
            Bon += 1
        else :
            CSm.append(CS[i])
            Em.append(E[i])
    
    Eff_CS = [0] * NB_COULEURS
    Eff_E = [0] * NB_COULEURS
    
    for i in range(NB_COULEURS) :
        Eff_CS[i] = CSm.count(i)
        Eff_E[i] = Em.count(i)
    
    for i in range(NB_COULEURS) :
        Mal += min(Eff_CS[i], Eff_E[i])
    
    return Bon, Mal

def arbitre2(CS, E) :
    VU_CS = [False] * NB_PIONS
    VU_E = [False] * NB_PIONS
    
    Bon = 0
    for i in range(NB_PIONS) :
        if CS[i] == E[i] :
            Bon += 1
            VU_CS[i] = True
            VU_E[i] = True
    
    Mal = 0
    for i in range(NB_PIONS) :
        for j in range(NB_PIONS) :
            if (i != j and not VU_CS[i] and not VU_E[j]
            and CS[i] == E[j]) :
                m += 1
                VU_CS[i] = True
                VU_E[j] = True
    
    return (Bon, Mal)

def getin() :
    return list(map(int, input("> ").split()))

from random import randint

def randcombi() :
    L = [0] * NB_PIONS
    for i in range(NB_PIONS) :
        L[i] = randint(0, NB_COULEURS - 1)
    return L

def SimPartie() :
    CS = randcombi()
    
    E = getin()
    nb = 1
    
    while E != CS :
        print(arbitre(CS, E))
        E = getin()
        nb += 1
    
    print("Combinaison trouvée en", nb,"essai(s).")

def LireEssai(S) :
    E = []
    elt = ""
    for i in range(1, len(S) - 1) :
        if S[i] == " " or S[i] == "," :
            if elt != "" :
                E.append(int(elt))
                elt = ""
        else :
            elt += S[i]
    if elt != "" :
        E. append(int(elt))
    return E
