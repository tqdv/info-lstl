from tkinter import Tk, Canvas, font

# ===================================
# La grille de jeu, initialement vide
# ===================================

M = 10 # lignes
N = 10 # colonnes

# On utilise la convention de notation des matrices
# +-->
# |
# v

def CréerGrille(m, n) :
    return [[0 for j in range(n)] for i in range(m)]

G = CréerGrille(M, N)


# ==========================
# Construction de la fenêtre
# ==========================

F = Tk()
F.title("2048")
FONT = font.Font(family="Arial", size=18, weight="bold")

TAILLE_CASE = 70

C = Canvas(F, width = N * TAILLE_CASE, height = M * TAILLE_CASE)
C.pack()

# Initialisation de la grille
Cases = [[None for _ in range(N)] for _ in range(M)]
Contenus = [[None for _ in range(N)] for _ in range(M)]
for i in range(M) :
    for j in range(N) :
        Cases[i][j] = C.create_rectangle(j * TAILLE_CASE, 
                                         i * TAILLE_CASE,
                                         (j + 1) * TAILLE_CASE,
                                         (i + 1) * TAILLE_CASE,
                                         fill="white")
        Contenus[i][j] = C.create_text(j * TAILLE_CASE + TAILLE_CASE // 2, i * TAILLE_CASE + TAILLE_CASE // 2, text="", font=FONT)
          
                     
# ===================
# Dessin de la grille
# ===================

# Liste des couleurs
COULEURS = ["#fff", "#f7b", "#bef", "#f0f", "#fee", "#9f9", "#c99", "#ad3", "#f88", "#fd0", "#f90"]

# Returns a luminosity value
# Alternative way to do it : use ord()
def Lum(c) :
    r = int(c[1], 16)
    g = int(c[2], 16)
    b = int(c[3], 16)
    
    return 2 * r + 7 * g + b

def Texte(k) :
    if k == 0 :
        return ""
    else :
        return str(2 ** k)

def DessinerGrille() :
    for i in range(M) :
        for j in range(N) :
            C.itemconfig(Cases[i][j], fill=COULEURS[G[i][j]])
            if Lum(COULEURS[G[i][j]]) > 110 :
                C.itemconfig(Contenus[i][j], fill="black")
            else :
                C.itemconfig(Contenus[i][j], fill="white")
            C.itemconfig(Contenus[i][j], text = Texte(G[i][j]))


# ================================
# Apparition d'éléments aléatoires
# ================================

def CasesVides() :
    L = []
    for i in range(M) :
        for j in range(N) :
            if G[i][j] == 0 :
                L.append((i, j))
    return L

from random import randint as AléaEnt

def Apparaître() :
    V = CasesVides()
    valeur = AléaEnt(1, 2) # Inclusive
    index = AléaEnt(0, len(V) -1)
    
    (i, j) = V[index]
    G[i][j] = valeur


# Copie de la grille
def Copie() :
    out = []
    for i in G :
        out.append(list(i))
    return out


# =========================
# Modification de la grille
# =========================

def Comparer(A, B) :
    for i in range(len(A)) :
        for j in range(len(A[i])) :
            if A[i][j] != B[i][j] :
                return False
    return True

# Poussée d'une liste vers les petits indices
def Pousser(L) :
    length = len(L)
    l = list(L)
    tmpl = []
    # Enlève tous les 0
    for i in l :
        if i != 0 :
            tmpl.append(i)
    #print(tmpl)
    
    l = tmpl
    i = 1
    tmpl = []
    if len(l) > 0 :
        while i < len(l) :
            if l[i-1] == l[i] :
                tmpl.append(l[i] + 1)
                i += 2
            else :
                tmpl.append(l[i-1])
                i += 1
        if i == len(l):
            tmpl.append(l[i - 1])

    # Pad with zeroes
    while (len(tmpl) < length) :
        tmpl.append(0)
    #print(tmpl)
    L = tmpl
    return L
    
# Extraction d'une ligne vers la droite
def ExtraireLigneVersDroite(i) :
    out =[]
    for j in range(N-1, 0 -1, -1) :
        out.append(G[i][j])
    return out

# Écrasement d'une ligne vers la droite
def ÉcraserLigneVersDroite(i, L) :
    for j in range(N) :
        G[i][N-1-j] = L[j]


# Poussée vers la droite
def PousserDroite() :
    B = Copie()
    for i in range(M) :
        ÉcraserLigneVersDroite(i, Pousser(ExtraireLigneVersDroite(i)))
    return not Comparer(G, B)

# Extraction d'une ligne vers la gauche
def ExtraireLigneVersGauche(i) :
    out =[]
    for j in range(N) :
        out.append(G[i][j])
    return out

# Écrasement d'une ligne vers la gauche
def ÉcraserLigneVersGauche(i, L) :
    for j in range(0, N) :
        #print("G[", i, "][", j, "] = L[", j, "]", sep='')
        G[i][j] = L[j]

# Poussée vers la gauche
def PousserGauche() :
    B = Copie()
    for i in range(M) :
        ÉcraserLigneVersGauche(i, Pousser(ExtraireLigneVersGauche(i)))
    return not Comparer(G, B)
    
# Extraction d'une ligne vers le haut
def ExtraireLigneVersHaut(j) :
    out =[]
    for i in range(M) :
        out.append(G[i][j])
    return out
# Écrasement d'une ligne vers la droite
def ÉcraserLigneVersHaut(j, L) :
    for i in range(M) :
        G[i][j] = L[i]
        
# Poussée vers le haut
def PousserHaut() :
    B = Copie()
    for j in range(N) :
        ÉcraserLigneVersHaut(j, Pousser(ExtraireLigneVersHaut(j)))
    return not Comparer(G, B)

# Extraction d'une ligne vers le bas
def ExtraireLigneVersBas(j) :
    out =[]
    for i in range(M -1, 0 -1, -1) :
        out.append(G[i][j])
    return out
# Écrasement d'une ligne vers le bas
def ÉcraserLigneVersBas(j, L) :
    for i in range(M) :
        G[M-1-i][j] = L[i]
        
# Poussée vers le bas
def PousserBas() :
    B = Copie()
    for j in range(N) :
        ÉcraserLigneVersBas(j, Pousser(ExtraireLigneVersBas(j)))
    return not Comparer(G, B)

# =================================
# Gestion des événements du clavier
# =================================

def ActionClavier(e) :
    if e.keysym == "Right" :
        if PousserDroite() :
            Apparaître()
    if e.keysym == "Left" :
        if PousserGauche() :
            Apparaître()
    if e.keysym == "Up" :
        if PousserHaut() :
            Apparaître()
    if e.keysym == "Down" :
        if PousserBas() :
            Apparaître()
           
    # Et on rafraîchit l'affichage
    DessinerGrille()
    F.update()


# Boucle principale
F.bind("<KeyPress>", ActionClavier)
Apparaître()
DessinerGrille()
F.mainloop()
                