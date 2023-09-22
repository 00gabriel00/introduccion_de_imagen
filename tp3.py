import tkinter as tk
from tkinter import filedialog
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

def cargar_imagenes():
    global imagen,imagenyiq
    ruta1 = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif")])
    
    if ruta1 :
        imagen= imageio.imread(ruta1)
        imagen = np.clip(imagen / 255., 0., 1.)
        imagenyiq=rgb_a_yiq(imagen)
def mostrar_imagenes():
    global imagen
    filtro = filtro_var.get()
    image_filtro = aplicar_filtro(imagen, filtro)
    plt.figure(figsize=(10, 5))
    
    plt.subplot(121)
    plt.imshow(imagen)
    plt.title("Imagen 1")
    
    plt.subplot(122)
    plt.imshow(image_filtro)
    plt.title(f"Imagen con filtro {filtro.capitalize()}")
    
    plt.tight_layout()
    plt.show()

def aplicar_filtro(image, filter_type):
    # Convertir la imagen a YIQ
    yiq_image = rgb_a_yiq(image)

    # Aplicar el filtro en el canal Y (luminancia)
    if filter_type == 'raiz':
        yiq_image[:, :, 0] = np.sqrt(yiq_image[:, :, 0])
    elif filter_type == 'cuadrado':
        yiq_image[:, :, 0] = np.square(yiq_image[:, :, 0])
    elif filter_type == 'lineal_a_trozos':
        yiq_image[:, :, 0] = np.where(yiq_image[:, :, 0] < 0.5, yiq_image[:, :, 0] * 2, 1.0 - 2.0 * (1.0 - yiq_image[:, :, 0]))

    # Convertir la imagen de nuevo a RGB
    image_result = yiq_a_rgb(yiq_image)

    return   image_result

def rgb_a_yiq(imagen):
    imagen_yiq = np.zeros(imagen.shape)
    imagen_yiq[:, :, 0] = np.clip(
        0.229 * imagen[:, :, 0] + 0.587 * imagen[:, :, 1] + 0.114 * imagen[:, :, 2],
        a_min=0,
        a_max=1
    )
    imagen_yiq[:, :, 1] = np.clip(
        0.595716 * imagen[:, :, 0] + -0.274453 * imagen[:, :, 1] + -0.321263 * imagen[:, :, 2],
        a_min=-0.5957,
        a_max=0.5957
    )
    imagen_yiq[:, :, 2] = np.clip(
        0.211456 * imagen[:, :, 0] + -0.522591 * imagen[:, :, 1] + 0.311135 * imagen[:, :, 2],
        a_min=-0.5226,
        a_max=0.5226
    )
    return  imagen_yiq
def yiq_a_rgb(imagen):
    imagen_rgb = np.zeros(imagen.shape)
    imagen_rgb[:, :, 0] = imagen[:, :, 0] + 0.9663 * imagen[:, :, 1] + 0.6210 * imagen[:, :, 2]
    imagen_rgb[:, :, 1] = imagen[:, :, 0] + -0.2721 * imagen[:, :, 1] + -0.6474 * imagen[:, :, 2]
    imagen_rgb[:, :, 2] = imagen[:, :, 0] + -1.1070 * imagen[:, :, 1] + 1.7046 * imagen[:, :, 2]
    imagen_rgb = (imagen_rgb* 255).astype(int)
    return np.clip(imagen_rgb, 0, 255)
    



imagen1 = None
imagen2 = None
imagen1yiq = None
imagen2yiq = None
#  se crear la ventana principal
ventana = tk.Tk()
ventana.title("Operaciones con Imágenes")

# Botón para cargar imágenes
boton_cargar = tk.Button(ventana, text="Cargar Imágenes", command=cargar_imagenes)
boton_cargar.pack()
filtro_var = tk.StringVar(ventana)
filtro_var.set("Filtro")  # Operación predeterminada

# Crear el menú desplegable para seleccionar la operación
operacion_menu = tk.OptionMenu(ventana, filtro_var, 'raiz', 'cuadrado', 'lineal_a_trozos')
operacion_menu.pack()

# Crear un botón para calcular
calcular_button = tk.Button(ventana, text="filtrar", command= mostrar_imagenes)
calcular_button.pack()
ventana.mainloop()

# Botones para realizar operaciones
