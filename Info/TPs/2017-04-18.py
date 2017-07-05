from numpy import matrix, zeros

A = matrix([
[3.0, -2.0],
[7.0, -6.0]
])

b = matrix([
[1.0],
[1.0]
])

# Li <-> Lj
def EchangerLignes(A, i, j) :
    (m, n) = A.shape
    for k in range(0, n) :
        A[i, k], A[j, k] = A[j, k], A[i, k]

# Ci <-> Cj
def EchangerCollones(A, i, j) :
    (m, n) = A.shape
    for k in range(0, m) :
        A[k, i], A[k, j] = A[k, j], A[k, i]

# Li <- lamba Li
def lLigne(A, i, l) :
    (m, n) = A.shape
    for k in range(n) :
        A[i, k] = l * A[i, k]

def lColonne(A, i, l) :
    (m, n) = A.shape
    for k in range(m) :
        A[k, i] = l * A[k, i]


def CLigne(A, i, j, l) :
    (m, n) = A.shape
    for k in range(n) :
        A[i, k] += l * A[j, k]

def CColonne(A, i, j, l) :
    (m, n) = A.shape
    for k in range(m) :
        A[k, i] += l * A[k, j]

def ResoudreTriangulaire(U, b) :
    (m, n) = U.shape
    x = matrix(zeros([n, 1]))
    
    for k in range(n-1, -1, -1) :
        x[k, 0] = b[k, 0]
        
        for j in range(k+1, n) :
            x[k, 0] -= U[k, j] * x[j, 0]
        
        x[k, 0] /= U[k, k]
    
    return x

def Resoudre(A, b) :
    (m, n) = A.shape
    
    for k in range(0, n-1) :
        
        i0 = k
        for i in range(k+1, n) :
            if abs(A[i, k]) > abs(A[i0, k]) :
                i0 = i
        EchangerLignes(A, k, i0)
        EchangerLignes(b, k, i0)
        
        if abs(A[k, k]) < 1e-6 :
            raise Exception("Systeme non inversible")
        
        
        for i in range(k+1, n) :
            pivot = -A[i, k] / A[k, k]
            CLigne(A, i, k, pivot)
            CLigne(b, i, k, pivot)
    return ResoudreTriangulaire(A, b)

