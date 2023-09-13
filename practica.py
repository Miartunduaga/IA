#PAG PRACTICA
import tkinter as tk
import limon as l
import uva as u
import papa as p


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
   
    if variable.get()== 0:
        ventanaP.withdraw()#Ocultar Pagina
        p.ventanap.deiconify()
        p.entrada_estado_fruta(variableEstado.get())
    elif variable.get()== 1:
        ventanaP.withdraw()
        u.ventanaU.deiconify()#mostrar pagina de Uva
        u.entrada_estado_fruta(variableEstado.get())
    elif variable.get() == 2:
        ventanaP.withdraw()
        l.llamarLimon()
        l.entrada_estado_fruta(variableEstado.get())
        
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

maduro = tk.Button(ventanaP, text="FRUTA MADURA", width=20, height=5,command=lambda: variableEstado.set(0))
inmaduro = tk.Button(ventanaP, text="FRUTA NO MADURA", width=20, height=5,command=lambda :variableEstado.set(1))

guardarEstado=tk.Button(ventanaP,text="GUARDAR ESTADO",width=10,height=5,command=caso)


papa = tk.Button(ventanaP, text="PAPA", width=20, height=5,command=lambda : variable.set(0))
uva = tk.Button(ventanaP, text="UVA", width=20, height=5,command=lambda : variable.set(1))
limon = tk.Button(ventanaP, text="LIMON", width=20, height=5,command=lambda : variable.set(2))

guardar = tk.Button(ventanaP,text="GUARDAR FRUTA",width=10,height=3,command=ocultarBotones)

guardar.place(x=500,y=500)
papa.place(x=230, y=100)
uva.place(x=230, y=200)
limon.place(x=230, y=300)




