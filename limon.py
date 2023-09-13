import tkinter as tk
from PIL import Image, ImageTk
import practica as p
import json
import os
import numpy as np
import matplotlib.pyplot as plt
from perceptronProfe import PerceptronProfe

ventanaL = tk.Tk()
ventanaL.title("PERCEPTRON LIMON")
ventanaL.geometry("600x600")
ventanaL.withdraw()

def llamarLimon():
    ventanaL.deiconify()


datosJSON=[]

entradaInicio=None
variableL=None

def llamarInicio(entradaClase):
    global entradaInicio
    entradaInicio = entradaClase

def capturar_area(event):
    x, y = event.x, event.y
    area = []
    for i in range(x - 3, x + 4):
        fila = []
        for j in range(y - 3, y + 4):
            try:
                color_pixel = imagen.getpixel((i, j))
                fila.append(color_pixel)
            except IndexError:
                fila.append((255, 255, 255))  # Si está fuera de la imagen, usar blanco
        area.append(fila)

#    Supongamos que 'area' contiene tus datos de 7x7 (49 valores)
#    Calcula el promedio de R, G y B
    suma_r = 0
    suma_g = 0
    suma_b = 0    
    
    for fila in area:
        print(fila)
    for fila in area:
        for r,g,b in fila:
            suma_r+=r
            suma_g+=g
            suma_b+=b
            print(f"R: {r}, G: {g}, B: {b}")
    totalPixeles=49
    
    print(f"total de pixeles    {totalPixeles},         suma R : {suma_r}     ,  suma g : {suma_g},        suma b : {suma_b}")
    
    promedio_r = suma_r // totalPixeles
    promedio_g = suma_g // totalPixeles
    promedio_b = suma_b // totalPixeles
    
    print(f"promedio R : {promedio_r}  ,   promedio G :   {promedio_g}   ,   promedio B   {promedio_b}")
    
    datos_json = []  # Declarar datos_json como una lista vacía aquí
    
    if os.path.exists("datosLimon.json"):
       #ABRIR UN JSON
       with open("datosLimon.json"  ,"r") as archivo_json:
            datos_json=json.load(archivo_json)
            
            ultimo_dato = datos_json[-1]
            iteracion = ultimo_dato["Indice"] 
            datos_json.append({
                "Indice":iteracion+1,
                "R":promedio_r,
                "G":promedio_g,
                "B":promedio_b,
                "Clase":variableL
            })             
    else:
        datos_json.append({
            "Indice": 1,
            "R":promedio_r,
            "G":promedio_g,
            "B":promedio_b,
            "Clase":variableL
        })

    # Guardar los datos en un archivo JSON
    with open("datosLimon.json", "w") as archivo_json:
        json.dump(datos_json, archivo_json, indent=4)
        print("Datos guardados en datosLimon.json")
        
def entrada_estado_fruta(entradaClase):
    global variableL
    rutaImagen =None
    variableL = entradaClase
    print(variableL)    
    if(variableL==0):
        rutaImagen="Frutas/Manzana/manzanaMadura.jpeg"
    else:
      rutaImagen="Frutas/Manzana/manzanaInmadura.jpeg"
    cargarImagen(rutaImagen)
    
print("VIDA HPTA QUE MUESTRA PRIMERO    ",variableL)
def cargarImagen(rutaImagen):
    global imagen
    global imagen_tk
    imagen = Image.open(rutaImagen)
    imagen = imagen.resize((600, 600))
    imagen_tk = ImageTk.PhotoImage(imagen)

    label_imagen = tk.Label(ventanaL, image=imagen_tk)
    label_imagen.pack(fill="both", expand=True)
    label_imagen.bind("<Button-1>", capturar_area)


# Función para retroceder al inicio
def retroceder_al_inicio(event):
    ventanaL.withdraw()  # Ocultar la ventana de práctica
    p.mostrarBotones()
    p.ventanaP.deiconify()  # Mostrar la ventana de inicio
    
# Vincular la función de retroceso al evento de teclado "Escape"
ventanaL.bind("<Escape>", retroceder_al_inicio)


'''
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


datosEtiqueta.append((etiqueta))
datosR.append(lista_R)
datosG.append(lista_G)
datosB.append(lista_B)



perceptron_LimonProfe = PerceptronProfe(3)

#perceptron_LimonProfe.propagacion(123,123,123)
perceptron_LimonProfe.entrenador(datosR,datosG,datosB,datosEtiqueta)


# Realizar predicciones
predicciones = []
for i in range(len(datosR)):
    prediccion = perceptron_LimonProfe.propagacion(datosR[i], datosG[i], datosB[i])
    predicciones.append(prediccion)

# Comparar con las etiquetas reales
correctos = np.sum(predicciones == etiqueta)
total = len(datosR)

# Calcular precisión
precision = correctos / total

# Imprimir resultados
print(f"Predicciones: {predicciones}")
print(f"Etiquetas reales: {etiqueta}")
print(f"Total de ejemplos: {total}")
print(f"Ejemplos clasificados correctamente: {correctos}")
print(f"Precisión: {precision}")







exactitud = 0
total_ejemplos = len(datos_para_entrenarlo)

for xi, etiqueta_real in datos_para_entrenarlo:
    prediccion = perceptron_LimonProfe.propagacion(xi)
    if prediccion == etiqueta_real:
        exactitud += 1

exactitud /= total_ejemplos

print("Exactitud en el conjunto de prueba:", exactitud)



#PERCEPTRON COLORES RGB 
perceptron_Limon =perceptron(3)

with open('datosLimon.json','r') as archivo_json:
        datos =json.load(archivo_json)
datos = datos[:-30]

ejemplos= np.array([[dato['R'],dato['G'],dato['B'],dato['Clase']]for dato in datos])

print(ejemplos.shape,"AHSASDBOASHDANDSANHSDNASDNASN")

epocas =10
grad_pesosL = [perceptron_Limon.pesos]



for epoca in range (0,100):
    for i in range(0,49):
        perceptron_Limon.propagacion(ejemplos[i,0:3])
        perceptron_Limon.actualizacionCoeficiente(0.5,ejemplos[i,3])
        grad_pesosL = np.concatenate((grad_pesosL,[perceptron_Limon.pesos]),axis =0)

#ANALISIS PARA COMPROBAR SI ESTTA MRD FUNCIONA O NO SIUUUUUUU
with open('datosLimon.json','r') as archivo_js:
    datosExamen = json.load(archivo_js)
    ultimos_elementos = datosExamen[-30:]

# Evaluación de los últimos ejemplos
for datos in ultimos_elementos:
    entradas = [datos['R'], datos['G'], datos['B']]
    salida_esperada = datos['Clase']  # Supongamos que 0 representa maduro y 1 representa inmaduro
    
    # Propaga las entradas a través del perceptrón
    perceptron_Limon.propagacion(entradas)
    
    # Verifica si la salida del perceptrón coincide con la salida esperada
    if perceptron_Limon.salida == salida_esperada:
        print("Predicción correcta:", perceptron_Limon.salida)
    else:
        print("Predicción incorrecta. Salida del perceptrón:", perceptron_Limon.salida)
    
    


for epoca in range(epocas):
    for ejemplo in ejemplos:
        entradas = ejemplo[:3]# toma los 3 primeros datos del arreglo ejemplos porque el ultimo dato es la clase,0 si es madura 1 si es inmadura
        salidaDeseada= ejemplo[3]#aqui toma el ultimo dato del arreglo ejemplo que es 0 o 1
        perceptron_Limon.propagacion(entradas)
        perceptron_Limon.actualizacionCoeficiente(0.1,salidaDeseada)#aqui entra la actualizacion de pesos # el ritmo es de 0.5 y entra la salida deseada
        
        
        grad_pesosLimon = np.concatenate((grad_pesosL,[perceptron_Limon.pesos]),axis =0)


plt.plot(grad_pesosL[:,0],'k')
plt.plot(grad_pesosL[:,1],'r')
plt.plot(grad_pesosL[:,2],'b')
plt.show()
        
'''        

