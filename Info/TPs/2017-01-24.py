from tkinter import *

F = Tk()
F.title("Un bouton")

def Destroy() :
    F.destroy()

def Coucou() :
    textePetiteZone.set("Coucou !")

def Calculer() :
    text_saisieResult.set( str(eval(text_saisieCalcul.get())) )

def setMaj() :
    textePetiteZone.set(textePetiteZone.get().upper())

boutonDestroy = Button(F, text="Close", command=Destroy)
boutonDestroy.pack()

textePetiteZone = StringVar()
saisiePetiteZone = Entry(F, textvariable=textePetiteZone, width=120 )
saisiePetiteZone.pack()

boutonTest = Button(F, text="default", command=Coucou)
boutonTest.pack()

bouttonMaj = Button(F, text="Mettre en Majuscule", command=setMaj)
bouttonMaj.pack()

text_saisieCalcul = StringVar()
saisieCalcul = Entry(F, textvariable=text_saisieCalcul, width=120)
saisieCalcul.pack()

text_saisieResult = StringVar()
saisieResult = Entry(F, textvariable=text_saisieResult, width=120)
saisieResult.pack()

boutonCalculer = Button(F, text="Calculer", command=Calculer)
boutonCalculer.pack()

P = Canvas(F, width=500, height=500, bg="lightgrey")
P.pack()

def Hexd(x) :
    return hex(x)[2:4].zfill(2)

def RGB(q,w,e) :
    return "#" + Hexd(int(255*q)) + Hexd(int(255*w)) + Hexd(int(255*e))

def Dessiner() :
    P.create_line(100, 100, 100, 400)
    P.create_line(100, 400, 400, 400)
    P.create_line(100, 100, 400, 100)
    P.create_line(400, 100, 400, 400)

def DessDiag() :
    P.create_polygon(100, 300, 300, 100, 500, 300, 300, 500, fill="green", outline="purple")

def DessDiagLine() :
    for x in range(0,500) :
        for y in range(0,500) :
            lamb = x / 500
            mu = y / 500
            P.create_line(x, y, x+1, y+1, fill=RGB(1-lamb, mu, 1-mu))


boutonTest2 = Button(F, text="Dessiner", command=Dessiner)
boutonTest2.pack()

boutonTest3 = Button(F, text="Diag", command=DessDiag)
boutonTest3.pack()

boutonTest4 = Button(F, text="Diag", command=DessDiagLine)
boutonTest4.pack()

def Circles() :
    for x in range(0,500) :
        for y in range(0, 500) :
            
            if (x - 250)**2 + (y - 100)**2 <= 300**2 :
                red = -1
            else :
                red = 0

            if (x - 100)**2 + (y - 400)**2 <= 300**2 :
                green = -1
            else :
                green = 0

            if (x - 400)**2 + (y - 400)**2 <= 300**2 :
                blue = -1
            else :
                blue = 0


            P.create_line(x, y, x+1, y+1, fill=RGB(1-red, 1-green, 1-blue))
 
boutonTest4 = Button(F, text="Circ", command=Circles)
boutonTest4.pack()

F.mainloop()


