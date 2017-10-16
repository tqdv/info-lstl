# ANALYSE FRÉQUENTIELLE DES MOTS DANS UN TEXTE

# str.isalpha()
# str.lower()

def SéparerMots(Texte) :
    L = []
    cstr = ""
    
    for i in Texte :
        if i.isalpha() :
            cstr += i.lower()
        else :
            if cstr != "" :
                L.append(cstr)
                cstr = ""
    
    if cstr != "" :
        L.append(cstr)
    
    return L

# s.join(L) concatène la liste L des caractères séparée par s
# Avec "rb", contenu est une liste de bytes

ARBRE_VIDE = None

# Ajoute l'occurence du mot dans l'arbre binaire de recherche, de noeud (mot, effectif)
def Ajouter(mot, A) :
    if A == ARBRE_VIDE :
        return ((mot, 1), ARBRE_VIDE, ARBRE_VIDE)
    
    else :
        ((n, e), g, d) = A
        if mot == n :
            return ((n, e +1), g, d)
        
        elif mot < n :
            return ((n, e), Ajouter(mot, g), d)
        
        elif mot > n :
            return ((n, e), g, Ajouter(mot, d))

# Parcours un arbre dans le sens précisé
def Parcourir(A, sens = "infixe") :
    L = []
    
    if A == ARBRE_VIDE :
        pass
    
    else :
        (n, g, d) = A
        if sens == "infixe" :
            L += Parcourir(g, sens) + [n] + Parcourir(d, sens)
        
        elif sens == "préfixe" :
            L += [n] + Parcourir(g, sens) + Parcourir(d, sens)
        
        elif sens == "postfixe" :
            L += Parcourir(g, sens) + Parcourir(d, sens) + [n]

    return L

def Tri(L, Comp) :
    # Implémentation du tri fusion
    if len(L) <= 1 :
        return L
    else :
        S = []
        
        m = len(L) // 2
        A = Tri(L[:m], Comp)
        B = Tri(L[m:], Comp)
        
        i = 0; j = 0
        a = len(A) ; b = len(B)
        while i < a and j < b :
            if Comp(A[i], B[j]) :
                S.append(A[i])
                i += 1
            else :
                S.append(B[j])
                j += 1
        
        S += A[i:] + B[j:]
        
        return S

# Compare les effectifs des mots
def Comp(a, b) :
    (_, ae) = a
    (_, be) = b
    return ae < be

# Renvoie une liste (mot, effectif) des mots d'un fichier
def AnalyserFichier(adresse) :
    with open(adresse, "rb") as fichier :
        contenu = fichier.read()
    
    Texte = "".join([ chr(o) for o in contenu ])
    Mots = SéparerMots(Texte)
    
    A = ARBRE_VIDE
    for m in Mots :
        A = Ajouter(m, A)
    L = Parcourir(A)
    L = Tri(L, Comp)
    
    return L
# E = AnalyserFichier(<adresse>)

# Filtre les mots ne satisfaisant pas P
# F pour Fréquences des mots
def unP(F, P) :
    L = []
    
    for (m, e) in F :
        if P(m) :
            L.append((m, e))
    
    return L

def contientX(m) :
    for i in m :
        if i == "x" :
            return True
    return False
# unP(E, contientX)

def contientDoubleConsonne(m) :
    i = 0
    while i +1 < len(m) :
        if m[i] == m[i +1] and not m[i] in "aeiouàéèù":
            return True
        i += 1
    return False
# unP(E, contientDoubleConsonne)

# Garde que les mots présents dans M
def sontDans(F, M) :
    # Trie M et F dans l'ordre alphabétique
    def CompM(x, y) :
        return x < y
    def CompF(x, y) :
        (xm, _) = x
        (ym, _) = y
        
        return xm < ym
    M = Tri(M, CompM)
    F = Tri(F, CompF)
        
    # Returne -1, 0, 1 quand m inférieur, égal, supérieur à mf
    def compMF(m, f) :
        (mf, ef) = f
        if m < mf :
            return -1
        elif m == mf :
            return 0
        elif m > mf :
            return 1
    
    L = []
    i = 0 ; j = 0
    m = len(M) ; f = len(F)
    while i < m and j < f :
        cmp = compMF(M[i], F[j])
        
        if cmp == 0 :
            L.append(F[j])
            i += 1 ; j += 1
        elif cmp == -1 :
            i += 1
        elif cmp == 1 :
            j += 1
    
    return L
