#PAG UVA

import tkinter as tk
import cv2 as c 
from PIL import Image,ImageTk

ventanaU=tk.Tk()
ventanaU.title("PERCEPTRON UVA")
ventanaU.withdraw()   #Oculta ventana del inicio
ventanaU.geometry("600x600")

variableU=None

def entrada_estado_fruta(entradaClase):
    global variableU
    variableU =entradaClase
    print(variableU)

