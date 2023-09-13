import tkinter as tk


ventanap = tk.Tk()
ventanap.title("PERCEPTRON PAPA")
ventanap.geometry("600x600")
ventanap.withdraw()

variableP=None

def entrada_estado_fruta(entradaClase):
    global variableP
    variableP =entradaClase
    print(variableP)

