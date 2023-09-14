import tkinter as tk
import cv2 as c
from PIL import Image, ImageTk
import numpy as np
import json
import os
import practica as p
#import practica as p

ventanaLimonEntrada = tk.Tk()
ventanaLimonEntrada.title("PERCEPTRON LIMON")
ventanaLimonEntrada.geometry("600x600")
ventanaLimonEntrada.withdraw()

ventanaMostrar =None
variableL=None

etiquetaVideo= tk.Label(ventanaLimonEntrada)#papi se supone que ya saben como es un label

etiquetaVideo.pack()#el pack hace que automaticamente la etiqueta se posicione por defecto en la ventana

def llamarLimon():
    ventanaLimonEntrada.deiconify()

#Funcion para actualizar el video en tkinter
def actualizarVideo():
    global ventanaMostrar
    confirmarCaptura,ventanaMostrar= cap.read() #confirmarCaptura nos dice si la conexion funciono o no /TrueOrFalse,ventanaMostrar recibe tambien los datos de capRead()que son los pixeles que se mostraran del video
    if confirmarCaptura:
        #tenemos que convertir el frame de OpenCV de BGR A RGB, para que sea compatible con nuestros datos.
        ventanaMostrar=c.cvtColor(ventanaMostrar,c.COLOR_BGR2RGB)
        ventanaMostrar=c.resize(ventanaMostrar,(600,600))
        #lo que hacemos aqui es para que el frame de openCV se adapte ala ventan tkinter
        foto=ImageTk.PhotoImage(image=Image.fromarray(ventanaMostrar))
        #Actualizamos la etiqueta con la imagen ya adaptada para tkinter
        etiquetaVideo.config(image=foto)
        etiquetaVideo.foto = foto
        etiquetaVideo.after(10,actualizarVideo)#cada 0.01 segundos se actualiza el video o el label


def capturarArea(event):
    global ventanaMostrar
    
    x,y = event.x, event.y
    area= []
    for ancho in range(x-3,x+4):# o sea que empiece en la posicion X -3 y avance hasta x+4
        fila=[]
        for alto in range(y-3,y+4):
            try:
                imagen_pillow= Image.fromarray(ventanaMostrar)
                obtenerPixel =imagen_pillow.getpixel((ancho,alto))
                fila.append(obtenerPixel)
            except IndexError:
                fila.append((255,255,255))#pos si se sale de la imagen recoja datos en blanco pero es imposible aparentementeeeeeeeeeeee
        area.append(fila)# aqui la lista fila se agrega a la lista area
    suma_r=0
    suma_g=0
    suma_b=0
    '''
    for fila in area:
       print(fila)#para mostrar los datos 
    '''
    for fila in area:
        for r,g,b in fila:
            suma_r+=r
            suma_g+=g
            suma_b+=b
            
           # print(f"R: {r}, G: {g}, B: {b}")
    totalPixeles= 49
    
   # print(f"total de pixeles    {totalPixeles},         suma R : {suma_r}     ,  suma g : {suma_g},        suma b : {suma_b}")
    
    promedioR =suma_r//totalPixeles    
    promedioG =suma_g//totalPixeles    
    promedioB =suma_b//totalPixeles    
    
   # print(f"promedio R : {promedioR}  ,   promedio G :   {promedioG}   ,   promedio B   {promedioB}")
    print(f" LOS DATOS QUE SUELTA LA FUNCION CAPTURAR AREA {promedioR},    {promedioG},   {promedioB}")
    
    datos_json=[]
    if os.path.exists("datosLimon.json"):
       #ABRIR UN JSON
       with open("datosLimon.json"  ,"r") as archivo_json:
            datos_json=json.load(archivo_json)
            
            ultimo_dato = datos_json[-1]
            iteracion = ultimo_dato["Indice"] 
            datos_json.append({
                "Indice":iteracion+1,
                "R":promedioR,
                "G":promedioG,
                "B":promedioB,
                "Clase":variableL
            })             
    else:
        datos_json.append({
            "Indice": 1,
            "R":promedioR,
            "G":promedioG,
            "B":promedioB,
            "Clase":variableL
        })
    with open("datosLimon.json",'w') as archivo_json:
        json.dump(datos_json,archivo_json,indent=4)
        print("SE GUARDARON LOS DATOS")


# Función para retroceder al inicio
def retroceder_al_inicio(event):
    ventanaLimonEntrada.withdraw()  # Ocultar la ventana de práctica
    p.mostrarBotones()
    p.ventanaP.deiconify()  # Mostrar la ventana de inicio
    
# Vincular la función de retroceso al evento de teclado "Escape"
ventanaLimonEntrada.bind("<Escape>", retroceder_al_inicio)
    
    
def entradaMaduraOInmadura(entradaEstado):
    global variableL
    variableL=entradaEstado

# Inicializa la camara o la fuente de video
cap = c.VideoCapture('http://192.168.18.9:4747/video')

actualizarVideo()
etiquetaVideo.bind("<Button-1>",capturarArea)
#ventanaLimonEntrada.mainloop()