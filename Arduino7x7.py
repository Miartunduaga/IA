from PIL import Image, ImageTk
import tkinter as tk

coordenadas_clic = []
cuadro_px = 7
ventana = tk.Tk()

imagen_original = Image.open(r"D:\Universidad\10 semestre\IA\Images\descargar.jpeg")
imagen = ImageTk.PhotoImage(imagen_original)

lienzo = tk.Canvas(ventana, width=imagen.width(), height=imagen.height())
lienzo.pack()


def manejar_clic(event):
    x_clic, y_clic = event.x, event.y
    coordenadas_clic.append((x_clic, y_clic))

    # Asegurarse de que el cuadro no se desborde fuera de los límites de la imagen
    x_inicio = max(x_clic - cuadro_px // 2, 0)
    y_inicio = max(y_clic - cuadro_px // 2, 0)
    x_final = min(x_clic + cuadro_px // 2, imagen_original.width)
    y_final = min(y_clic + cuadro_px // 2, imagen_original.height)

    # Obtener el cuadro de píxeles de 7x7
    cuadro = imagen_original.crop((x_inicio, y_inicio, x_final, y_final))

    # Obtener los valores RGB del cuadro
    rgb_valores = list(cuadro.getdata())

    print(f"Coordenada del clic: ({x_clic}, {y_clic})")
    print("Valores RGB del cuadro de 7x7:")
    for fila in range(cuadro_px):
        fila_rgb = rgb_valores[fila * cuadro_px : (fila + 1) * cuadro_px]
        print(fila_rgb)


lienzo.create_image(0, 0, anchor=tk.NW, image=imagen)

lienzo.bind("<Button-1>", manejar_clic)

ventana.mainloop()
