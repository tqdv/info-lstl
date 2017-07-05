from tkinter import Tk, Canvas, PhotoImage
from numpy import cos, sin, pi

def Hexd(x) :
    return hex(x)[2:4].zfill(2)

def RGB(q,w,e) :
    return "#" + Hexd(int(255*q)) + Hexd(int(255*w)) + Hexd(int(255*e))




# Dimensions de la zone de dessin
WIDTH = 400 ; HEIGHT = 400

def DessinerOvale() :
    F = Tk()
    ZoneDessin = Canvas(F, width=WIDTH, height=HEIGHT)
    ZoneDessin.pack()
    Dessin = PhotoImage(width=WIDTH, height=HEIGHT)
    
    # Le dessin à faire
    A = WIDTH / 3 ; B = HEIGHT / 5
    for t in range(1000) :
        x = WIDTH // 2 + int( A * cos( 2* pi * t / 1000 ))
        y = HEIGHT // 2 + int( B * sin ( 2* pi * t / 1000 ))
        Dessin.put(RGB(1, 1, 0), (x, y))
    
    # Affichage
    ZoneDessin.create_image((1 + WIDTH //2 , 1 + HEIGHT //2), image=Dessin )
    F.mainloop ()

def DessSin() :
    F = Tk()
    ZoneDessin = Canvas(F, width=WIDTH, height=HEIGHT)
    ZoneDessin.pack()
    Dessin = PhotoImage(width=WIDTH, height=HEIGHT)
    
    # Le dessin à faire
    
    Amp = 100 ; puls = 0.1
    x_min = 0 ; x_max = WIDTH
    N = 10000
    
    for n in range(N) :
        t = x_min + (x_max - x_min) * n / N
        y = int(Amp * cos(puls*t)+ HEIGHT/2)
        x = int(t)
        Dessin.put(RGB(0, 0, 0), (x, y))

    
    # Affichage
    ZoneDessin.create_image((1 + WIDTH //2 , 1 + HEIGHT //2), image=Dessin )
    F.mainloop()

def DessDegr() :
    F = Tk()
    ZoneDessin = Canvas(F, width=WIDTH, height=HEIGHT)
    ZoneDessin.pack()
    Dessin = PhotoImage(width=WIDTH, height=HEIGHT)
    
    for y in range(HEIGHT) :
        for x in range(WIDTH) :
            Dessin.put(RGB(x / WIDTH, 1 - y / HEIGHT, 0), (x, y))
    
    ZoneDessin.create_image((1 + WIDTH //2 , 1 + HEIGHT //2), image=Dessin )
    F.mainloop()
        

from numpy.polynomial import Polynomial

def polypolypolypoly() :

    P = Polynomial([-1, 0, 1])
    print(P.coef)
    print(P.roots())
    print(P.deriv())

def estProche(z, zl, eps) :
    for i in range(len(zl)) :
        if abs(z - zl[i]) <= eps :
            return i
    return -1

def Comportement(z0, P, dP, zl, eps, n_max = 20) :
    z = z0
    for step in range(n_max) :
        root = estProche(z, zl, eps)
        if root != -1 :
            return step, root
        z = z - P(z) / dP(Z)
    
    return n_max, -1

def Newton(z0, P, dP, Z, eps, max) :
    zn = z0 ; n = 0
    znp1 = zn - P(zn) / dP(zn)
    while abs(znp1 - zn) > eps and n < max :
        zn = znp1 ; n += 1
        znp1 = zn - P(zn) / dP(zn)
    i = estProche(znp1, Z, 2 * eps)
    return n, i

def DessFrac(P, eps) :
    F = Tk()
    ZoneDessin = Canvas(F, width=WIDTH, height=HEIGHT)
    ZoneDessin.pack()
    Dessin = PhotoImage(width=WIDTH, height=HEIGHT)
    
    dP = P.deriv()
    Z = P.roots()
    
    x_min = -1
    x_max = 1
    y_min = -1
    y_max = 1
    
    max = 20
    
    Couleur = [
        (1,0,0),
        (0,1,0),
        (0,0,1)
        ]
    
    for x in range(WIDTH) :
        for y in range(HEIGHT) :
            z = (x_min + (x_max - x_min) * x / WIDTH
                + (y_min + (y_max - y_min) * y / HEIGHT) * 1j
                )
            n, i = Newton(z, P, dP, Z, eps, max)
            
            r, g, b = Couleur[i]
            r += (1 - r) * n / max
            g += (1 - g) * n / max
            b += (1 - b) * n / max
            
            Dessin.put(RGB(r,g,b), (x, y))
    
    ZoneDessin.create_image((1 + WIDTH //2 , 1 + HEIGHT //2), image=Dessin )
    F.mainloop()