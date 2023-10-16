#PAG PRACTICA
import tkinter as tk
import Entrenamiento as e

ventanaP = tk.Tk()

ventanaP.withdraw()
ventanaP.geometry("600x600")

entradaIndex=None

def ocultarBotones():
    papa.place_forget()
    uva.place_forget()
    limon.place_forget()
    guardar.place_forget()
    frutaMaestro.place_forget()
    
    if(entradaIndex==0):
        maduro.place(x=230, y=100)
        inmaduro.place(x=230, y=300)
        guardarEstado.place(x=500,y=500)
    elif(entradaIndex==1):
        caso()

def caso():
        ventanaP.withdraw()
        e.llamarLimon()
        e.entradaMaduraOInmadura(estadoYfruta())
        e.mostrarTitulo(variable.get())
def mostrarBotones():
   papa.place(x=230, y=100)
   uva.place(x=230, y=200)
   limon.place(x=230, y=300)
   guardar.place(x=500,y=500)
   frutaMaestro.place(x=230,y=400)
   
   maduro.place_forget()
   inmaduro.place_forget()
   guardarEstado.place_forget()


# Variable de control para el botón
variable = tk.IntVar()
variableEstado =tk.IntVar()

maduro = tk.Button(ventanaP, text="FRUTA MADURA", width=20, height=5,command=lambda: variableEstado.set(0))#valor 0 o sea que es maduro 
inmaduro = tk.Button(ventanaP, text="FRUTA NO MADURA", width=20, height=5,command=lambda :variableEstado.set(1))

guardarEstado=tk.Button(ventanaP,text="GUARDAR ESTADO",width=10,height=5,command=caso)


papa = tk.Button(ventanaP, text="PAPA", width=20, height=5,command=lambda : variable.set(0))
uva = tk.Button(ventanaP, text="UVA", width=20, height=5,command=lambda : variable.set(1))
limon = tk.Button(ventanaP, text="LIMON", width=20, height=5,command=lambda : variable.set(2))
frutaMaestro=tk.Button(ventanaP,text="FRUTA NUEVA",width=20,height=5,command=lambda:variable.set(3))

guardar = tk.Button(ventanaP,text="GUARDAR FRUTA",width=10,height=3,command=ocultarBotones)

def estadoYfruta():
    #variableEstado=MaduroInmaduro,varibale=PapaUvaLimonFrutaProfe entradaIndex=EntrenarClasificar
    arreglo=[variableEstado.get(),variable.get(),entradaIndex]
    return arreglo

def sacarClase(entradaI):
    global entradaIndex
    entradaIndex=entradaI

guardar.place(x=500,y=500)
papa.place(x=230, y=100)
uva.place(x=230, y=200)
limon.place(x=230, y=300)
frutaMaestro.place(x=230,y=400)

def retrocederInicio(event):
    from Index import mostrarVentana
    mostrarVentana()

def ocultarVentana():
    ventanaP.withdraw()
    
ventanaP.bind("<Escape>",retrocederInicio)


