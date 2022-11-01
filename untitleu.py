# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 10:40:49 2022

@author: lab
"""

import tkinter


def myFunction():
    etiqueta.confing(text="ups-2022")
    
def random():
    

raiz =tkinter.Tk()
raiz.title("POO-UPS")
boton = tkinter.Button(raiz,text= "Aceptar",background = "red")
etiqueta= tkinter.Label(raiz,text="hola mundo")


boton.pack() # pack es apilar 
etiqueta.pack()
raiz.mainloop()