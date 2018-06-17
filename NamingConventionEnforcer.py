#################################################################
#
# NaminConventionEnforcer: to keep game asset names as standard
#                           as possible
# Autor: Homar Orozco Apaza
#################################################################

import tkinter
import os

var1, var2, var3, var4, var5, var6, var7 = 'Gakou','Kabe','4m','1f','Soto','Mado','Hiroi'

def CadenaModelo(E1,E2,E3,E4,E5,E6,E7):
    cadena="SM_{}-{}-{}{}{}-{}{}".format(E1,E2,E3,E4,E5,E6,E7)
    borrame = tkinter.Tk()
    borrame.withdraw()
    borrame.clipboard_clear()
    borrame.clipboard_append(cadena)
    borrame.update()
    borrame.destroy()
    print(cadena)

def CadenaMaterial(E8, E9, E10, E11):
    cadena="MI_{}-{}-{}-{}".format(E8, E9, E10, E11)
    borrame = tkinter.Tk()
    borrame.withdraw()
    borrame.clipboard_clear()
    borrame.clipboard_append(cadena)
    borrame.update()
    borrame.destroy()
    print(cadena)

def CadenaTextura(E8, E9, E10, E11):
    cadena="T_{}-{}-{}-{}_".format(E8, E9, E10, E11)
    borrame = tkinter.Tk()
    borrame.withdraw()
    borrame.clipboard_clear()
    borrame.clipboard_append(cadena)
    borrame.update()
    borrame.destroy()
    print(cadena)

def main():
    raiz = tkinter.Tk()
    raiz.title("Naming Convention enforcer")

    tkinter.Label(raiz,text="MODELOS:", fg="blue").grid(row=0,column=0)

    tkinter.Label(raiz,text="MundoOpack").grid(row=1,column=0)
    tkinter.Label(raiz,text="-QueCosaEs").grid(row=1,column=1)
    tkinter.Label(raiz,text="-Geometria").grid(row=1,column=2)
    tkinter.Label(raiz,text="Posicion1").grid(row=1,column=3)
    tkinter.Label(raiz,text="Posicion2").grid(row=1,column=4)
    tkinter.Label(raiz,text="-Contiene").grid(row=1,column=5)
    tkinter.Label(raiz,text="Variacion").grid(row=1,column=6)

    E1 = tkinter.Entry(raiz, width=20, bd=5)
    E1.insert(0,var1)
    E1.grid(row=2,column=0)
    E2 = tkinter.Entry(raiz, width=20, bd=5)
    E2.insert(0,var2)
    E2.grid(row=2,column=1)
    E3 = tkinter.Entry(raiz, width=20)
    E3.insert(0,var3)
    E3.grid(row=2,column=2)
    E4 = tkinter.Entry(raiz, width=20, bd=5)
    E4.insert(0,var4)
    E4.grid(row=2,column=3)
    E5 = tkinter.Entry(raiz, width=20)
    E5.insert(0,var5)
    E5.grid(row=2,column=4)
    E6 = tkinter.Entry(raiz, width=20)
    E6.insert(0,var6)
    E6.grid(row=2,column=5)
    E7 = tkinter.Entry(raiz, width=20, bd=5)
    E7.insert(0,var7)
    E7.grid(row=2,column=6)

    tkinter.Button(raiz, text="Create Chain", command=lambda:CadenaModelo( E1.get(),E2.get(),E3.get(),E4.get(),E5.get(),E6.get(),E7.get() )).grid(row=3,column=0)

    tkinter.Label(raiz,text="MATERIALS & TEXTURES:", fg="blue").grid(row=4,column=0)

    tkinter.Label(raiz,text="MundoOpack").grid(row=5,column=0)
    tkinter.Label(raiz,text="QueCosaEs").grid(row=5,column=1)
    tkinter.Label(raiz,text="Posicion1").grid(row=5,column=3)
    tkinter.Label(raiz,text="Variacion").grid(row=5,column=6)

    E8 = tkinter.Entry(raiz, width=20)
    E8.insert(0,var1)
    E8.grid(row=6,column=0)
    E9 = tkinter.Entry(raiz, width=20)
    E9.insert(0,var2)
    E9.grid(row=6, column=1)
    E10 = tkinter.Entry(raiz, width=20)
    E10.insert(0,var4)
    E10.grid(row=6,column=3)
    E11 = tkinter.Entry(raiz, width=20)
    E11.insert(0,var7)
    E11.grid(row=6,column=6)
    
    tkinter.Button(raiz, text="Material", command=lambda:CadenaMaterial( E8.get(), E9.get(), E10.get(), E11.get() )).grid(row=7,column=0)
    tkinter.Button(raiz, text="Textura", command=lambda:CadenaTextura( E8.get(), E9.get(), E10.get(), E11.get() )).grid(row=7,column=1)

    raiz.mainloop()


if __name__ == "__main__" : main()
