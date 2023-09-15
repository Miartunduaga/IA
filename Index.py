#PAG INDEX
import tkinter as tk
import practica as pa

global variableDesicion
variableDesicion =tk.IntVar()

ventana = tk.Tk()
ventana.geometry("600x600")
ventana.title("TEXTO PRUEBA")

def abrir_Practica():
    #Ocultar Pagina
    ventana.withdraw()
    #Mostrar Pagina
    pa.ventanaP.deiconify()
    pa.sacarClase(variableDesicion.get())
    print(variableDesicion.get()," ENTRENAMIENTO   0    ,    CLASIFICACION    1")



etiqueta = tk.Label(ventana,text="HOLA MUNDO",bg="green")
etiqueta.pack(fill=tk.X)
#command=lambda:saludo   permite sincronizar funciones.
boton1=tk.Button(ventana, text="Practica",command=lambda:variableDesicion.set(0), width=10 ,height=10)
boton1.place(x=270,y=150)
boton1.pack()

boton2=tk.Button(ventana, text="CLASIFICACION",command=lambda :variableDesicion.set(1), width=10 ,height=10)
boton2.place(x=270,y=150)
boton2.pack()

boton3 =tk.Button(ventana,text="GUARDAR",command=abrir_Practica, width=10 ,height=10)
boton3.place(x=300,y=300)
ventana.mainloop()