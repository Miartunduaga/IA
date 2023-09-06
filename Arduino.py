from PIL import Image, ImageTk
import tkinter as tk

coordenadas_clic = []

def manejar_clic(event):
    if imagen:
        x_clic, y_clic = event.x, event.y
        if 0 <= x_clic < imagen.width() and 0 <= y_clic < imagen.height():
            coordenadas_clic.append((x_clic, y_clic))

            # Obtener el valor RGB de la coordenada del clic
            color = imagen_original.getpixel((x_clic, y_clic))
            r, g, b = color

            print(f"Coordenada del clic: ({x_clic}, {y_clic})")
            print(f"Valor RGB en la coordenada: ({r}, {g}, {b})")
    
ventana = tk.Tk()

imagen_original = Image.open(r"D:\Universidad\10semestre\IA\Images\descargar.jpeg")
imagen = ImageTk.PhotoImage(imagen_original)

lienzo = tk.Canvas(ventana, width=imagen.width(), height=imagen.height())
lienzo.pack()

lienzo.create_image(0, 0, anchor=tk.NW, image=imagen)

lienzo.bind("<Button-1>", manejar_clic)

ventana.mainloop()
