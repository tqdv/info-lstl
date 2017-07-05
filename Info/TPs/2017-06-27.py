VIDE = 0
BLANC = 1
NOIR = 2
DAME_B = 3
DAME_N = 4


def Initialiser() :
    G = [[VIDE for _ in range(10) ] for _ in range(10) ]
    
    # Blancs
    for i in range(0, 4) :
        for j in range(5) :
            G[i][2 * j + i % 2] = BLANC
    
    # Noirs
    for i in range(6, 10) :
        for j in range(5) :
            G[i][2 * j + i % 2] = NOIR
    
    return G

G = Initialiser()

# Modélisation d'un coup
MV_SIMPLE = 10
PRISE = 11
MV_DAME = 12
PRISE_DAME = 13
PROMO = 14


def Prisespossibles(i, j, c) :
    # Deuxième couleur
    c_ = BLANC + NOIR - c
    
    #
    H = [[ False for j in range(10)] for i in range(10)]
    H [i][j] = True
    
    def ExploreDepuis(i_, j_) :
        Trouve = False
        
        if (i_ >= 2 and j_ >= 2 and G[i_ -1][j_ -1] == c_
            G[i_ -2][j_ -2] == VIDE and not H[i_-1][j_-1]) :
            
            Trouve = True
            Chemin.append((i_-2, j_-2))
            H[i_-1][j_-1] = True
            
            ExploreDepuis(i_-2, j_-2)
            
            H[i_-1][j_-1] = False
            Chemin.pop()
        
        if (i_ <= 7 and j_ >= 2 and G[i_+1][j_-1] == c_
            G[i_ +2][j_ -2] == VIDE and not H[i_+1][j_-1]) :
            
            Trouve = True
            Chemin.append((i_-2, j_-2))
            H[i_-1][j_-1] = True
            
            ExploreDepuis(i_-2, j_-2)
            
            H[i_-1][j_-1] = False
            Chemin.pop()
        
        # ??
        if (i_ >= 2 and j_ >= 2 and G[i_ -1][j_ -1] == c_
            G[i_ -2][j_ -2] == VIDE and not H[i_-1][j_-1]) :
            
            Trouve = True
            Chemin.append((i_-2, j_-2))
            H[i_-1][j_-1] = True
            
            ExploreDepuis(i_-2, j_-2)
            
            H[i_-1][j_-1] = False
            Chemin.pop()
        
        #if 
        
        if not Trouve :
            prises.append((PRISE, list(Chemin)))

def CoupsPossibles(G, c) :
    P = []
    
    for i in range(10) :
        for j in range(10) :
            # Cas d'un pion
            if G[i][j] == c :
                if c == BLANC :
                    # On va vers les i croissants
                        if i < 8 and j > 0 and G[i +1][j -1] == VIDE :
                            P.append((MV_SIMPLE, [(i, j), (i+1, j-1)] ))
                        if i < 8 and j < 9 and G[i +1][j +1] == VIDE :
                            P.append((MV_SIMPLE, [(i, j), (i+1, j+1)] ))
                    
                    # Promotions
                    # ...
                    
                    # Prises
                    # ...
            # Cas d'une dame
            if G[i][j] == c + 2 :
                pass
                # ...
    
    return P

from random import randint as EntAlea

def StratAlea(P) :
    # Liste des prises
    Prises = []
    for p in P :
        if p[0] == PRISE or p[0] == PRISE_DAME :
            Prises.append(p)
    
    # Si aucun, on choisit au hasard
    if Prises == [] :
        return P[EntAlea(0, len(P) -1)]
    # Sinon, prises maximales
    else :
        Max = [Prises[0]]
        
        for k in range(1, len(Prises)) :
            if len(Prises[k][1]) > len(Max[0][1]) :
                Max = [Prises[k]]
            elif len(Prises[k][1]) == len(Max[0][1]) :
                Max.append(Prises[k])

        return Max[EntAlea(0, len(Max) -1)]

def Jouer(G, coup) :
    if coup[0] == MV_SIMPLE :
        # v contient la case de départ et d'arrivée
        L = coup[1]
        
        # Départ
        (i,j) = L[0]
        c = G[i][j] # pion
        G[i][j] = VIDE
        
        # Arrivée
        (i, j) = L[1]
        G[i][j] = c
    elif coup[0] == PRISE :
        pass
        # ...
    # ...
