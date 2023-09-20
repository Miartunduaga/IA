#PAG ENTRENAMIENTO
import tkinter as tk
import cv2 as c
from PIL import Image, ImageTk
import numpy as np
import json
import os
import practica as p
from perceptronProfe import PerceptronProfe
import time as t
import sys
import pandas as pd
import serial
from time import sleep

ser = serial.Serial('COM4', 9600)
sleep(5)


ventanaLimonEntrada = tk.Tk()

ventanaLimonEntrada.geometry("600x600")
ventanaLimonEntrada.withdraw()


ventanaMostrar =None
variableL=[]

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
            

    totalPixeles= 49
    
   
    promedioR =suma_r//totalPixeles    
    promedioG =suma_g//totalPixeles    
    promedioB =suma_b//totalPixeles    
    print(f"EL PROMEDIO QUE DA DE LOS COLORES ES :    R:   {promedioR}   G: {promedioG}  B: {promedioB}")
    
    if variableL[2]==0:
        "ESTAS EN MODO ENTRENAMIENTO"
        datosParaEntrenar(promedioR,promedioG,promedioB)
    elif variableL[2]==1:
        
        print("ESTAS CLASIFICANDO")
        
        clasificar(promedioR,promedioG,promedioB)
        

# Función para retroceder al inicio
def retroceder(event):
    ventanaLimonEntrada.withdraw()  # Ocultar la ventana de práctica
    p.mostrarBotones()
    p.ventanaP.deiconify()  # Mostrar la ventana de inicio

def datosParaEntrenar(r,g,b):
    datos_json=[]
    if(variableL[1]==2):
        if os.path.exists("datosLimon.json"):
       #ABRIR UN JSON
            with open("datosLimon.json","r") as archivo_json:
                datos_json=json.load(archivo_json)
            
                ultimo_dato = datos_json[-1]
                iteracion = ultimo_dato["Indice"] 
                datos_json.append({
                    "Indice":iteracion+1,
                    "R":r,
                    "G":g,
                    "B":b,
                    "Clase":variableL[0]
            })             
        else:
            datos_json.append({
                "Indice": 1,
                "R":r,
                "G":g,
                "B":b,
                "Clase":variableL[0]
        })
        with open("datosLimon.json",'w') as archivo_json:
            json.dump(datos_json,archivo_json,indent=4)
            print("SE GUARDARON LOS DATOS DE LIMON")
    elif(variableL[1]==0):
        if os.path.exists("datosPapa.json"):
       #ABRIR UN JSON
            with open("datosPapa.json"  ,"r") as archivo_json:
                datos_json=json.load(archivo_json)
            
                ultimo_dato = datos_json[-1]
                iteracion = ultimo_dato["Indice"] 
                datos_json.append({
                    "Indice":iteracion+1,
                    "R":r,
                    "G":g,
                    "B":b,
                    "Clase":variableL[0]
            })             
        else:
            datos_json.append({
                "Indice": 1,
                "R":r,
                "G":g,
                "B":b,
                "Clase":variableL[0]
        })
        with open("datosPapa.json",'w') as archivo_json:
            json.dump(datos_json,archivo_json,indent=4)
            print("SE GUARDARON LOS DATOS DE PAPA")
    elif (variableL[1]==1):
        if os.path.exists("datosUva.json"):
       #ABRIR UN JSON
            with open("datosUva.json","r") as archivo_json:
                datos_json=json.load(archivo_json)
            
                ultimo_dato = datos_json[-1]
                iteracion = ultimo_dato["Indice"] 
                datos_json.append({
                    "Indice":iteracion+1,
                    "R":r,
                    "G":g,
                    "B":b,
                    "Clase":variableL[0]
            })             
        else:
            datos_json.append({
                "Indice": 1,
                "R":r,
                "G":g,
                "B":b,
                "Clase":variableL[0]
        })
        with open("datosUva.json",'w') as archivo_json:
            json.dump(datos_json,archivo_json,indent=4)
            print("SE GUARDARON LOS DATOS DE UVA")
    elif (variableL[1]==3):
        if os.path.exists("datosFrutaProfe.json"):
       #ABRIR UN JSON
            with open("datosFrutaProfe.json","r") as archivo_json:
                datos_json=json.load(archivo_json)
            
                ultimo_dato = datos_json[-1]
                iteracion = ultimo_dato["Indice"] 
                datos_json.append({
                    "Indice":iteracion+1,
                    "R":r,
                    "G":g,
                    "B":b,
                    "Clase":variableL[0]
            })             
        else:
            datos_json.append({
                "Indice": 1,
                "R":r,
                "G":g,
                "B":b,
                "Clase":variableL[0]
        })
        with open("datosFrutaProfe.json",'w') as archivo_json:
            json.dump(datos_json,archivo_json,indent=4)
            print("SE GUARDARON LOS DATOS DE LA NUEVA FRUTA")
    
def entradaMaduraOInmadura(entradaEstado):
    global variableL
    variableL=entradaEstado
    print(variableL[2])


# Inicializa la camara o la fuente de video
cap = c.VideoCapture('http://192.168.100.20:4747/video')


etiquetaVideo= tk.Label(ventanaLimonEntrada)#papi se supone que ya saben como es un label

etiquetaVideo.pack()#el pack hace que automaticamente la etiqueta se posicione por defecto en la ventana

actualizarVideo()
etiquetaVideo.bind("<Button-1>",capturarArea)

ventanaLimonEntrada.bind("<Escape>",retroceder)


def clasificar(r,g,b):
    global variableL
    with open(f'{nombreArchivoJson[variableL[1]]}','r') as archivo_json:
        datosCargados=json.load(archivo_json)
    lista_R=np.array([datos['R']for datos in datosCargados])
    lista_G=np.array([datos['G']for datos in datosCargados])
    lista_B=np.array([datos['B']for datos in datosCargados])
    etiqueta=np.array([datos['Clase']for datos in datosCargados])
    
    nuevo_data = {
        'r' : lista_R,
        'g' : lista_G,
        'b' : lista_B,
        'clase' : etiqueta
    }
    
    df = pd.DataFrame(nuevo_data)
    #df.to_excel('archivo.xlsx', index=False, engine='openpyxl')
    
    if(variableL[1]==2):
        perceptronLimon= PerceptronProfe(3)
        perceptronLimon.limpiarHistorial()
        perceptronLimon.entrenador(lista_R,lista_G,lista_B,etiqueta)
        print("PERCEPTRON LIMON CLASIFICANDO")
        t.sleep(3)
        salidaPerceptron=perceptronLimon.propagacion(r,g,b)
        comprobarSiFunciona(salidaPerceptron)
        perceptronLimon.mostrarGraficoPesos()
        df.to_excel('archivo_Limon.xlsx', index=False, engine='openpyxl')
    elif(variableL[1]==0):
        perceptronPapa = PerceptronProfe(3)
        perceptronPapa.limpiarHistorial()
        perceptronPapa.entrenador(lista_R,lista_G,lista_B,etiqueta)
        print("PERCEPTRON PAPA CLASIFICANDO")
        t.sleep(3)
        salidaPerceptron=perceptronPapa.propagacion(r,g,b)
        comprobarSiFunciona(salidaPerceptron)
        perceptronPapa.mostrarGraficoPesos()
        df.to_excel('archivo_Papa.xlsx', index=False, engine='openpyxl')
    elif(variableL[1]==1):
        perceptronUva = PerceptronProfe(3)
        perceptronUva.limpiarHistorial()
        perceptronUva.entrenador(lista_R,lista_G,lista_B,etiqueta)
        print("PERCEPTRON UVA CLASIFICANDO")
        t.sleep(3)
        salidaPerceptron=perceptronUva.propagacion(r,g,b)
        comprobarSiFunciona(salidaPerceptron)
        perceptronUva.mostrarGraficoPesos()
        df.to_excel('archivo_Uva.xlsx', index=False, engine='openpyxl')

    elif(variableL[1]==3):
        perceptronFruta = PerceptronProfe(3)
        perceptronFruta.limpiarHistorial()
        perceptronFruta.entrenador(lista_R,lista_G,lista_B,etiqueta)
        print("PERCEPTRON FRUTA DEL MAESTRO CLASIFICANDO")
        t.sleep(3)
        salidaPerceptron=perceptronFruta.propagacion(r,g,b)
        comprobarSiFunciona(salidaPerceptron)
        perceptronFruta.mostrarGraficoPesos()
        df.to_excel('archivo_Fruta.xlsx', index=False, engine='openpyxl')


def comprobarSiFunciona(salida):
    if salida==0:
        print("LA FRUTA ES MADURA")
        entrada = 1
        ser.write(str(entrada).encode())
    else:
        print("LA FRUTA ES INMADURA")
        
nombreArchivoJson= ['datosPapa.json','datosUva.json','datosLimon.json','datosFrutaProfe.json']

nombreTitulo=['papa','uva','limon','frutaProfe']

def mostrarTitulo(variable):
    x =variable
    ventanaLimonEntrada.title("perceptron " + nombreTitulo[x])
    
#ventanaLimonEntrada.mainloop()