#PAG INDEX
import tkinter as tk
import practica as pa

ventana = tk.Tk()
ventana.geometry("600x600")
ventana.title("INICIO DE CLASIFICACION")


def abrir_Practica():
    #Ocultar Pagina
    ventana.withdraw()
    #Mostrar Pagina
    if variableDesicion.get()==0:
        pa.ventanaP.title("PRACTICA")
    elif variableDesicion.get()==1:
        pa.ventanaP.title("CLASIFICACION")
    
    
    pa.ventanaP.deiconify()
    pa.sacarClase(variableDesicion.get())
    print(variableDesicion.get()," ENTRENAMIENTO   0    ,    CLASIFICACION    1")



etiqueta = tk.Label(ventana,text="HOLA MUNDO",bg="green")
etiqueta.pack(fill=tk.X)
#command=lambda:saludo   permite sincronizar funciones.
boton1=tk.Button(ventana, text="Practica",command=lambda:variableDesicion.set(0), width=15 ,height=5)
boton1.place(x=270,y=150)

boton2=tk.Button(ventana, text="CLASIFICACION",command=lambda :variableDesicion.set(1), width=15 ,height=5)
boton2.place(x=270,y=250)


boton3 =tk.Button(ventana,text="GUARDAR",command=abrir_Practica, width=10 ,height=5)
boton3.place(x=500,y=500)

def mostrarVentana():
    ventana.deiconify()
    pa.ocultarVentana()

global variableDesicion
variableDesicion =tk.IntVar()
ventana.mainloop()