#PAG PRACTICA
import tkinter as tk
import Entrenamiento as e


ventanaP = tk.Tk()
ventanaP.title("PRACTICA")
ventanaP.withdraw()
ventanaP.geometry("600x600")


def ocultarBotones():
    papa.place_forget()
    uva.place_forget()
    limon.place_forget()
    guardar.place_forget()
    
    maduro.place(x=230, y=100)
    inmaduro.place(x=230, y=300)
    guardarEstado.place(x=500,y=500)

def caso():
        ventanaP.withdraw()
        e.llamarLimon()
        e.entradaMaduraOInmadura(estadoYfruta())
        
def mostrarBotones():
   papa.place(x=230, y=100)
   uva.place(x=230, y=200)
   limon.place(x=230, y=300)
   guardar.place(x=500,y=500)
   
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

guardar = tk.Button(ventanaP,text="GUARDAR FRUTA",width=10,height=3,command=ocultarBotones)

def estadoYfruta():
    arreglo=[variableEstado.get(),variable.get()]
    return arreglo

guardar.place(x=500,y=500)
papa.place(x=230, y=100)
uva.place(x=230, y=200)
limon.place(x=230, y=300)




