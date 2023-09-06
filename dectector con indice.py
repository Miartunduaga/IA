from PIL import Image, ImageTk
import tkinter as tk

coordenadas_clic = []
cuadro_px = 7
imagen_original = None
promedios_rgb = {} 

def calcular_promedio(valores_rgb):
    total_r = 0
    total_g = 0
    total_b = 0
    Salida = 0

    for r, g, b in valores_rgb:
        total_r += r
        total_g += g
        total_b += b
        
    Salida=input("Digite salida")
    Salida=int(" "+ Salida)

    num_pixeles = len(valores_rgb)
    promedio_r = total_r // num_pixeles
    promedio_g = total_g // num_pixeles
    promedio_b = total_b // num_pixeles

    return promedio_r, promedio_g, promedio_b, Salida

def manejar_clic(event):
    global imagen_original
    x_clic, y_clic = event.x, event.y
    coordenadas_clic.append((x_clic, y_clic))

    x_inicio = max(x_clic - cuadro_px // 2, 0)
    y_inicio = max(y_clic - cuadro_px // 2, 0)

    try:
        x_final = min(x_clic + cuadro_px // 2, imagen_original.width)
        y_final = min(y_clic + cuadro_px // 2, imagen_original.height)
    except AttributeError:
        print("Error: No se ha abierto una imagen.")
        return

    cuadro = imagen_original.crop((x_inicio, y_inicio, x_final, y_final))

    rgb_valores = list(cuadro.getdata())

    print(f"Coordenada del clic: ({x_clic}, {y_clic})")
    
    promedio_rgb = calcular_promedio(rgb_valores)

    promedios_rgb[len(coordenadas_clic)] = promedio_rgb

ventana = tk.Tk()

try:
    imagen_original = Image.open(r"D:\Universidad\10 semestre\IA\Images\descargar.jpeg")
except FileNotFoundError:
    print("Error: No se pudo encontrar la imagen 'descargar.jpeg'")
    ventana.quit()

imagen = ImageTk.PhotoImage(imagen_original)

lienzo = tk.Canvas(ventana, width=imagen.width(), height=imagen.height())
lienzo.pack()

lienzo.create_image(0, 0, anchor=tk.NW, image=imagen)

lienzo.bind("<Button-1>", manejar_clic)

ventana.mainloop()

print("Promedios RGB con índices:", promedios_rgb)

