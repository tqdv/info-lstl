# 2017-01-18

## Topic: maze made of horizontal lines and vertical lines.


# Dimensions du labyrinthe
nbLignes = 10 # lignes
nbColonnes = 15
 # colonnes

# +-----------> colonne
# |
# |
# |
# |
# |
# v
#  
# i


# Types de parois
RIEN = 0
MUR = 1
BORD = 2

# Creation d'in labyrinthe plein de murs
def LabyrinthePlein() :
    # Parois horizontales
    PH = [ [ MUR for colonne in range(0,nbColonnes)] for ligne in range(0,nbLignes+1) ]
    for ligne in range(0,nbColonnes) :
        PH[0][ligne] = BORD
        PH[nbLignes][ligne] = BORD
    # Parois verticales
    PV = [ [ MUR for colonne in range(0,nbColonnes+1) ] for ligne in range(0,nbLignes) ]
    for ligne in range(0,nbLignes) :
        PV[ligne][0] = BORD
        PV[ligne][nbColonnes] = BORD
    return (PH, PV)

# Dessin d'un labyrinthe
from matplotlib.pyplot import axis, plot, show

def Dessiner(Labyrinthe) :
    (PH, PV) = Labyrinthe
    
    axis([-1, nbColonnes+1, -nbLignes -1, 1]) # Pour la visibilite
    
    # Parois horizontales
    for ligne in range(0,nbLignes+1) :
        for colonne in range(0,nbColonnes) :
            if PH[ligne][colonne] == MUR :
                plot( [colonne, colonne+1], [-ligne, -ligne], color=(0,0,0))
            if PH[ligne][colonne] == BORD :
                plot( [colonne, colonne+1], [-ligne, -ligne], color=(0,0,0), linewidth = 2)
    # Parois verticales
    for ligne in range(0,nbLignes) :
        for colonne in range(nbColonnes+1) :
            if PV[ligne][colonne] == MUR :
                plot( [colonne, colonne], [-ligne, -ligne-1], color=(0,0,0))
            if PV[ligne][colonne] == BORD :
                plot( [colonne, colonne], [-ligne, -ligne-1], color=(0,0,0), linewidth = 2)

# Experience de Bernouilli
from random import random

def Bernoulli(p) :
    return random() < p

# Labyrinthes aleatoires
def SupprimerMurs(Labyrinthe, p) :
    (PH, PV) = Labyrinthe
    
    # Parois horizontales
    for ligne in range(0,nbLignes+1) :
        for colonne in range(0,nbColonnes) :
            if PH[ligne][colonne] == MUR and Bernoulli(p):
                PH[ligne][colonne] = RIEN
    
    # Parois verticales
    for ligne in range(0,nbLignes) :
        for colonne in range(nbColonnes+1) :
            if PV[ligne][colonne] == MUR and Bernoulli(p):
                PV[ligne][colonne] = RIEN
    return (PH, PV)

def CasesAdjacentesSansLabel(case, Labyrinthe, Balisage):
    V = []
    ( PH, PV ) = Labyrinthe
    (lign, col) = case
    
    # Haut
    if lign > 0 and PH[lign][col] == RIEN and Balisage[lign -1][col] == -1 :
        V.append( (lign -1, col))
    # Bas
    if lign < nbLignes -1 and PH[lign+1][col] == RIEN and Balisage[lign+1][col] == -1 :
        V.append( (lign +1, col))
    # Gauche
    if col > 0 and PV[lign][col] == RIEN and Balisage[lign][col -1] == -1 :
        V.append( (lign, col -1))
    # Droite
    if col < nbColonnes -1 and PV[lign][col +1] == RIEN and Balisage[lign][col +1] == -1 :
        V.append( (lign, col +1))
    return V


def Baliser(A, Labyrinthe) :
    (lign_a, col_a) = A
    (lign_b, col_b) = B
    
    Balisage = [[-1 for i in range(nbColonnes)] for i in range(nbLignes) ]
    
    Balisage[lign_a][col_a] = 0
    dernCases = [(lign_a, col_a)]
    # dern = derniere
    distance = 1
    
    while dernCases != [] :
        nouv_dernCases = [] # nouveau
        
        for case in dernCases :
            for (lign, col) in CasesAdjacentesSansLabel(case, Labyrinthe, Balisage) :
                Balisage[lign][col] = distance
                nouv_dernCases.append( (lign, col) )
        distance += 1
        dernCases = list(nouv_dernCases)
    return Balisage
    
def AdjacentInferieur(case, Labyrinthe, Balisage):
    ( PH, PV ) = Labyrinthe
    (lign, col) = case
    
    distance = Balisage[lign][col]
    
    # Haut
    if lign > 0 and PH[lign][col] == RIEN and Balisage[lign -1][col] < distance :
        return (lign -1, col)
    # Bas
    if lign < nbLignes -1 and PH[lign+1][col] == RIEN and Balisage[lign+1][col] < distance :
        return (lign +1, col)
    # Gauche
    if col > 0 and PV[lign][col] == RIEN and Balisage[lign][col -1] < distance :
        return (lign, col -1)
    # Droite
    if col < nbColonnes -1 and PV[lign][col +1] == RIEN and Balisage[lign][col +1] < distance :
        return (lign, col +1)
    
def Chemin(Labyrinthe, Depart, Arrivee) :
    B = Baliser(Labyrinthe, Depart)
    (lign, col) = Arrivee
    L = []
    
    if B[lign][col] == -1 :
        return None
    else :
        distance = B[lign][col]
        while distance > 0 :
            
        
    


def Test() :
    L = LabyrinthePlein()
    L = SupprimerMurs(L, 0.5)
    Dessiner(L)
    show()
    print(Chemin ((1,1), (10,10), L))
    