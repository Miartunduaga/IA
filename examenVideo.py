import tkinter as tk
import cv2 as c
from PIL import Image, ImageTk
import numpy as np
import json
from PerceptronProfe import PerceptronProfe

ventanaE = tk.Tk()
ventanaE.title("PERCEPTRON LIMON")
ventanaE.geometry("600x600")

#ventanaE.withdraw() PARA OCULTAR LA PAGINA
ventanaMostrar =None
rojo=None
verde=None
azul=None


    
        
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
    '''
    rojo.append(promedioR)
    verde.append(promedioG)
    azul.append(azul)
    '''
    return promedioR,promedioG,promedioB
    
# Inicializa la camara o la fuente de video
cap = c.VideoCapture('http://192.168.18.9:4747/video')

etiquetaVideo= tk.Label(ventanaE)#papi se supone que ya saben como es un label

etiquetaVideo.pack()#el pack hace que automaticamente la etiqueta se posicione por defecto en la ventana



actualizarVideo()
etiquetaVideo.bind("<Button-1>",capturarArea)



#PERCEPTRON PROFESOR 

datosEtiqueta =[]
datosR=[]
datosG=[]
datosB=[]
with open('datosLimon.json','r') as archivos_json:
    datosCargados=json.load(archivos_json)
lista_R =np.array([datos['R']for datos in datosCargados])
lista_G =np.array([datos['G']for datos in datosCargados])
lista_B =np.array([datos['B']for datos in datosCargados])
etiqueta =np.array([datos['Clase']for datos in datosCargados])

#no hace nada diferente, a la listas lista_R,lista_G, lo unico que cambia es en la forma reducida para mostrar pero es lo mismo
datosEtiqueta.append((etiqueta))
datosR.append(lista_R)
datosG.append(lista_G)
datosB.append(lista_B)


perceptronLimon=PerceptronProfe(3)

#perceptronLimon.entrenador(lista_R,lista_G,lista_B,etiqueta)

perceptronLimon.entrenador(datosR,datosG,datosB,datosEtiqueta)
def activarExamenPerceptron(event):
    perceptronLimon.peso1(0.5)
    perceptronLimon.peso2(0.5)
    perceptronLimon.peso3(0.5)
    salidaPerceptron =perceptronLimon.propagacion(*capturarArea(event))
    
   # salidaPerceptron =perceptronLimon.propagacion(15,15,15)
    print(salidaPerceptron)


ventanaE.bind("<Return>",activarExamenPerceptron)
entrada = tk.Entry(ventanaE)
entrada.pack()

ventanaE.mainloop()

