from matplotlib.pyplot import plot , grid , show
from numpy import sqrt , exp , log as ln , sin , cos
from numpy import matrix , zeros

def Euler (F, t_0 , t_max , N, Y_0) :
    h = ( t_max - t_0) / N
    Y = matrix ( Y_0) ; TY = [ matrix (Y)]
    t = t_0 ; T = [t]
    for n in range (N) :
        Y += h * F(Y, t) ; TY. append ( matrix (Y))
        t += h ; T. append (t)
    return (T, TY)

v = matrix([
[1.5],
[-1.2],
[0.0],
])

d = 8
v2 = matrix(zeros([d, 1]))

# Recuperer composante
def RecupComp(TY, i) :
    return [ Y[i, 0] for Y in TY]

def F(Y, t) :
    d = 1
    out = matrix(zeros([d, 1]))
    
    out[0, 0] = Y[0, 0]
    
    return out

g = 9.8  # m.s-2
l = 0.25 # m

def F(Y, t) :
    d = 2
    Z = matrix ( zeros ([2, 1]))
    Z[0, 0] = Y[1, 0]
    Z[1, 0] = -g/l * sin(Y[0, 0])
    return Z

def EuExp() :
    t_0 = 0.
    t_max = 2.0
    N = 1000
    Y_0 = 1.0
    def F(Y, t) :
        d = 1
        out = matrix(zeros([d, 1]))
        out[0, 0] = Y[0, 0]    
        return out
    
    (T, TY) = Euler (F, t_0 , t_max , N, Y_0)
    plot(T, RecupComp(TY, 0), color='blue')
    
    
    t_0 = 0.0
    t_max = -2.0
    
    (L, LY) = Euler (F, t_0 , t_max , N, Y_0)
    plot(L, RecupComp(LY, 0), color='blue')
    
    x = [i/1000 -2 for i in range(4000)]
    y = [exp(i) for i in x]
    plot(x, y, color='red')


# Print graph
def printg() :
    grid(True)
    show()

def Pendule() :
    g = 9.8  # m.s-2
    l = 1.0 # m

    def F(Y, t) :
        d = 2
        Z = matrix ( zeros ([2, 1]))
        Z[0, 0] = Y[1, 0]
        Z[1, 0] = -g/l * sin(Y[0, 0])
        return Z
    
    t_0 = 0.0
    t_max = 50.0
    N = 1000
    Y_0 = matrix([[0.1], [0.0]])
    
    (T, TY) = Euler (F, t_0 , t_max , N, Y_0)
    plot(T, RecupComp(TY, 0), color='blue')

def Heun (F, t_0 , t_max , N, Y_0) :
    h = ( t_max - t_0) / N
    Y = matrix (Y_0) ; TY = [ matrix (Y)]
    t = t_0 ; T = [t]
    for n in range (N) :
        Y += h * (F(Y, t) + F(Y+h*F(Y, t), t+h)) /2
        TY.append( matrix(Y))
        
        t += h ; T. append (t)
    return (T, TY)

def PenduleHeu() :
    g = 9.8  # m.s-2
    l = 102.0 # m

    def F(Y, t) :
        d = 2
        Z = matrix ( zeros ([2, 1]))
        Z[0, 0] = Y[1, 0]
        Z[1, 0] = -g/l * sin(Y[0, 0])
        return Z
    
    t_0 = 0.0
    t_max = 500.0
    N = 100000
    Y_0 = matrix([[0.0001], [0.1]])
    
    (T, TY) = Heun (F, t_0 , t_max , N, Y_0)
    plot(T, RecupComp(TY, 0), color='blue')

