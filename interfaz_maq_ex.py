# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 10:01:56 2022

@author: lab
"""

from tkinter import *

raiz = Tk()

raiz.title("ventana de prueba")#titulo
raiz.resizable(1, 1) #ancho y alto width=0  height=0 funciona con true y false sirva par el ancho y alto de la ventana 
raiz.iconbitmap("expen.ico") # icono de la ventana
raiz.geometry("350x456")
raiz.config(bg="light green")
raiz = mainloop() # simepre debe estar en ultimo lugar ventana principal
