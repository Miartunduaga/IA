import cv2

# Lista para almacenar las coordenadas y los valores RGB
coordenadas = []

# Funcion para calcular el promedio del valor RGB
def calcularPromedioRGB(roi):
    b, g, r = cv2.split(roi)
    return (int(b.mean()), int(g.mean()), int(r.mean()))

# Funcion para manejar los eventos del mouse
def handle_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:  # Verifica si se hizo clic izquierdo
        roi = frame[y - 3:y + 4, x - 3:x + 4]  # Captura una region de 7x7 pixeles alrededor del clic
        if roi.shape == (7, 7, 3):
            # Calcula el promedio del valor RGB en la region
            rgb_average = calcularPromedioRGB(roi)
            # Almacena las coordenadas y el promedio en la lista
            coordenadas.append(((x, y), rgb_average))
            for coord, rgb in coordenadas:
                print(f"Coordenada: {coord}, Valor RGB Promedio: {rgb}")

# Inicializa la camara o la fuente de video
cap = cv2.VideoCapture('http://192.168.18.9:4747/video')

maicolpndj# Crea una ventana para mostrar el video
cv2.namedWindow("Video")
cv2.setMouseCallback("Video", handle_mouse)  # Establece la funcion de manejo del mouse

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Muestra el video en la ventana original
    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

# Muestra las coordenadas y los valores RGB promedio
for coord, rgb in coordenadas:
    print(f"Coordenada: {coord}, Valor RGB Promedio: {rgb}")
