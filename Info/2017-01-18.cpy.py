# 2017-01-18

## Topic: maze made of horizontal lines and vertical lines.


# Dimensions du labyrinthe
nbLignes = 10 # lignes
N = 15 # colonnes

# +-----------> j
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
    PH = [ [ MUR for j in range(0,N)] for ligne in range(0,nbLignes+1) ]
    for ligne in range(0,N) :
        PH[0][ligne] = BORD
        PH[nbLignes][ligne] = BORD
    # Parois verticales
    PV = [ [ MUR for j in range(0,N+1) ] for ligne in range(0,nbLignes) ]
    for ligne in range(0,nbLignes) :
        PV[ligne][0] = BORD
        PV[ligne][N] = BORD
    return (PH, PV)

# Dessin d'un labyrinthe
from matplotlib.pyplot import axis, plot, show

def Dessiner(Labyrinthe) :
    (PH, PV) = Labyrinthe
    
    axis([-1, N+1, -nbLignes -1, 1]) # Pour la visibilite
    
    # Parois horizontales
    for ligne in range(0,nbLignes+1) :
        for j in range(0,N) :
            if PH[ligne][j] == MUR :
                plot( [j, j+1], [-ligne, -ligne], color=(0,0,0))
            if PH[ligne][j] == BORD :
                plot( [j, j+1], [-ligne, -ligne], color=(0,0,0), linewidth = 2)
    # Parois verticales
    for ligne in range(0,nbLignes) :
        for j in range(N+1) :
            if PV[ligne][j] == MUR :
                plot( [j, j], [-ligne, -ligne-1], color=(0,0,0))
            if PV[ligne][j] == BORD :
                plot( [j, j], [-ligne, -ligne-1], color=(0,0,0), linewidth = 2)

L = LabyrinthePlein()
Dessiner(L)
show()