# ONLY FOR ARCHIVE PURPOSES

from matplotlib.pyplot import axis, grid, plot, scatter, show
from numpy import exp, sin, linspace, cos, pi

def drawsin(omega,amplitude, phi):
    X = linspace(-10,10,10000)
    Y = [ amplitude*sin(omega*x + phi) for x in X]
    
    grid(True) ; plot(X,Y,color='orange') ; show()

def drawsquare():
    X = [-1,0]
    Y = [0,1]
    plot(X,Y,color='red')
    
    X = [0,1]
    Y = [1,0]
    plot(X,Y,color='red')
    
    X = [-1,0]
    Y = [0,-1]
    plot(X,Y,color='red')
    
    X = [0,1]
    Y = [-1,0]
    plot(X,Y,color='red')
    
    grid(True) ; axis("equal") ;  show()

def drawtriangle() :
    X = [-0.5,0,0.5]
    Y = [0,0.866,0]
    plot(X,Y,color='red')
    X = [-0.5,0.5]
    Y = [0,0]
    plot(X,Y,color='red')
    grid(True) ; axis("equal") ;  show()

def drawcircle() :
    X = linspace(-1,1,1000)
    Y = [sqrt(1 - x**2) for x in X]
    plot(X,Y, color='red') ; 
    Y = [-sqrt(1 - x**2) for x in X]
    plot(X,Y,color='red') ; 
    grid(True) ; axis("equal") ; show()

def circul() :
    X = [cos(2*pi*i/4) for i in range(0,5)]
    Y = [sin(2*pi*i/4) for i in range(0,5)]
    plot(X,Y) ; axis("equal") ; grid(True) ; show()

def gradedcircle() :
    for radius in linspace(0,1,1000) :
        X = [radius*cos(2*pi*var/4) for var in linspace(0,4,100)]
        Y = [radius*sin(2*pi*var/4) for var in linspace(0,4,100)]
        
        coef = radius
        plot(X,Y,color=[coef,1-coef, coef])
    axis("equal") ; show()

def poly(n, radius):
    X = [radius*cos(2*pi*var/n) for var in range(0,n+1)]
    Y = [radius*sin(2*pi*var/n) for var in range(0,n+1)]
    plot(X,Y) ; axis("equal") ; grid(True) ; show()
    