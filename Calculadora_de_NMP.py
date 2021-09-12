# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 03:06:52 2021

@author: ruben
"""


import math as mt
import tkinter as tk

nmpt = {
  "0,0,0": "< 3",
  "0,0,1": 3,
  "0,1,0": 3,
  "1,0,0": 4,
  "1,0,1": 7,
  "1,1,0": 7,
  "1,1,1": 11,
  "1,2,0": 11,
  "2,0,0": 9,
  "2,0,1": 14,
  "2,1,0": 15,
  "2,1,1": 20,
  "2,2,0": 21,
  "2,2,1": 28,
  "3,0,0": 23,
  "3,0,1": 39,
  "3,0,2": 64,
  "3,1,0": 43,
  "3,1,1": 75,
  "3,1,2": 120,
  "3,2,0": 93,
  "3,2,1": 150,
  "3,2,2": 210,
  "3,3,0": 240,
  "3,3,1": 460,
  "3,3,2": 1100,
  "3,3,3": "≥ 2400"}

def nmpCal(num):
    nc = num.split(",")
    a = int(nc[0])
    b = int(nc[1])
    c = int(nc[2])
    return (((a+b+c)*100)/(mt.sqrt( ((3-a)*10 + (3-b)*1 + (3-c)*0.1) * 33.3)))
 
def NMP(num):
    try:
        return ("\n----  " + str(nmpt[num]) + " NMP/100 mL  ----\n")
    except:
        return ("\n----  " + str(round(nmpCal(num), 3)) + " NMP/100 mL  ----\n\nAdevertencia: el NMP no está en tablas y fue calculado")




    
    

ventana = tk.Tk()

ventana.author = "Rubén Téllez Gerardo"

ventana.title("NMP para coliformes")

#ventana.iconbitmap(r"C:\Programación ExL\Calculadora_NMP\tubo.ico")

ventana.geometry("300x500")
head = tk.Label(ventana, text = "Tablas - Cálculo para coliformes \nPara tubos con 10 mL, 1 mL y 0.1 mL (3 tubos cada uno)\nPor Rubén Téllez  v0.1.3 [3 decimales]", bg = "#faf0e6")
head.pack()





t1 = tk.Label(text = "\nTubos con 10 mL positivos:")
t1.pack()
ascr = tk.Scale(ventana, from_ = 0, to = 3, orient="horizontal")
ascr.pack()

def get_a():
    textoA = ascr.get()
    tr1["text"] = "-----> " + str(int(textoA)) + ' tubos con 10 mL'

#b_a = tk.Button(text = "Ver selección", padx = 10, pady = 5, command = get_a)
#b_a.pack()

tr1 = tk.Label()
tr1.pack()





t2 = tk.Label(text = "Tubos con 1 mL positivos:")
t2.pack()
bscr = tk.Scale(ventana, from_ = 0, to = 3, orient="horizontal")
bscr.pack()

def get_b():
    textoB = bscr.get()
    tr2["text"] = "-----> " + str(int(textoB)) + ' tubos con 1 mL'

#b_b = tk.Button(text = "Ver selección", padx = 10, pady = 5, command = get_b)
#b_b.pack()



tr2 = tk.Label()
tr2.pack()

t3 = tk.Label(text = "Tubos con 0.1 mL positivos:")
t3.pack()

cscr = tk.Scale(ventana, from_ = 0, to = 3, orient="horizontal")
cscr.pack()

def get_c():
    textoC = cscr.get()
    tr3["text"] = "-----> " + str(int(textoC)) + ' tubos con 1 mL'

#b_c = tk.Button(text = "Ver selección", padx = 10, pady = 5, command = get_c)
#b_c.pack()

tr3 =tk.Label()
tr3.pack()


inf = tk.Label(ventana,text = "Selecciona analizar para obtener el resultado", bg="pink")
inf.pack()



def analizar():
    a = int(ascr.get())
    b = int(bscr.get())
    c = int(cscr.get())
    resul["text"] = str(NMP((str(a) + "," + str(b) + "," + str(c))))
    
spa = tk.Label()
spa.pack()

b_an = tk.Button(text = "Analizar", padx = 10, pady = 10, command = analizar)
b_an.pack()

spa = tk.Label()
spa.pack()
    
resul = tk.Label(bg = "orange")
resul.pack()





ventana.mainloop()
