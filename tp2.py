import tkinter as tk
from tkinter import filedialog
import imageio.v2 as imageio
import matplotlib.pyplot as plt
import numpy as np

def cargar_imagenes():
    global imagen1, imagen2,imagen1yiq, imagen2yiq
    ruta1 = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif")])
    ruta2 = filedialog.askopenfilename(filetypes=[("Archivos de imagen", "*.png *.jpg *.jpeg *.bmp *.gif")])

    if ruta1 and ruta2:
        imagen1 = imageio.imread(ruta1)
        imagen1 = np.clip(imagen1 / 255., 0., 1.)


        imagen2 = imageio.imread(ruta2)
        imagen2 = np.clip(imagen2 / 255., 0., 1.)
        mostrar_imagenes()
        imagen1yiq=rgb_a_yiq(imagen1)
        imagen2yiq=rgb_a_yiq(imagen2)
def mostrar_imagenes():
    global imagen1, imagen2
    plt.figure(figsize=(10, 5))
    
    plt.subplot(121)
    plt.imshow(imagen1)
    plt.title("Imagen 1")
    
    plt.subplot(122)
    plt.imshow(imagen2)
    plt.title("Imagen 2")
    
    plt.tight_layout()
    plt.show()

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
    
#Lighte darker
def ifLighterRGB():
    global imagen1, imagen2
    rojo = np.maximum(imagen1[:, :, 0],imagen2[:, :, 0])
    verde = np.maximum(imagen1[:, :, 1], imagen2[:, :, 1])
    azul = np.maximum(imagen1[:, :, 2], imagen2[:, :, 2])
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(np.dstack((rojo, verde, azul)))
    plt.title("ifLighterRGB")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2")
    plt.tight_layout()
    plt.show()



def ifDarkerRGB():
    global imagen1, imagen2
    rojo = np.minimum(imagen1[:, :, 0],imagen2[:, :, 0])
    verde = np.minimum(imagen1[:, :, 1],imagen2[:, :, 1])
    azul = np.minimum(imagen1[:, :, 2],imagen2[:, :, 2])
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(np.dstack((rojo, verde, azul)))
    plt.title("ifLighterRGB")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2")
    plt.tight_layout()
    plt.show()


def ifLighterYIQ():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = np.where(im1_Y > im2_Y, im1_Y, im2_Y)
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("ifLighter YIQ")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()


def ifDarkerYIQ():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = np.where(im1_Y < im2_Y, im1_Y, im2_Y)
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("ifLighter YIQ")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()

def suma_imagenes():
    global imagen1, imagen2
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow((np.clip(((imagen1+imagen2) * 255).astype(int),0,255)))
    plt.title("suma de imagenes")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1 ")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2 ")
    plt.tight_layout()
    plt.show()

def resta_imagenes():
    global imagen1, imagen2
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow((np.clip(((imagen1-imagen2) * 255).astype(int),0,255)))
    plt.title("resta de imagenes rgb")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1 ")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2 ")
    plt.tight_layout()
    plt.show()
def suma_imagenespro():
    global imagen1, imagen2
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow((np.clip((((imagen1+imagen2)/2) * 255).astype(int),0,255)))
    plt.title("suma de imagenes")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1 ")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2 ")
    plt.tight_layout()
    plt.show()

def resta_imagenespro():
    global imagen1, imagen2
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow((np.clip((((imagen1-imagen2)/2) * 255).astype(int),0,255)))
    plt.title("resta de imagenes rgb")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1 ")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2 ")
    plt.tight_layout()
    plt.show()

def multiplicacion_imagenes():
    global imagen1, imagen2
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow((np.clip(((imagen1*imagen2) * 255).astype(int),0,255)))
    plt.title("producto de imagenes rgb")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1 ")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2 ")
    plt.tight_layout()
    plt.show()
def div_rgb():
    global imagen1, imagen2
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(np.clip(((imagen1/(imagen2*0.000001))* 255).astype(int),0,255))
    plt.title("division de imagenes rgb")
    plt.subplot(132)
    plt.imshow(imagen1)
    plt.title("imagen 1 ")
    plt.subplot(133)
    plt.imshow(imagen2)
    plt.title("imagen 2 ")
    plt.tight_layout()
    plt.show()
#suma clampeada
def suma_clampyiq():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = np.clip(im1_Y + im2_Y, None, 1)
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("suma clampeada")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()
#resta clampeada
def resta_clampyiq():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = np.clip(im1_Y - im2_Y, None, 1)
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("resta clampeada")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()
def resta_clampyiq_abs():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = np.clip(im1_Y - im2_Y, None, 1)
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(abs(np.dstack((res_Y, res_I, res_Q)))))
    plt.title("resta clampeada absoluto")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()
def suma_promiyq():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = (im1_Y + im2_Y)/2
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("suma promediada")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()
def resta_promyiq():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = (im1_Y - im2_Y)/2
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("resta promediada")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()
def resta_promyiq_abs():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = (im1_Y - im2_Y)/2
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(abs(np.dstack((res_Y, res_I, res_Q)))))
    plt.title("resta promediada absoluto")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()
def multiplicacion_yiq():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y =(im1_Y * im2_Y)
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("producto")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()
def multiplicacion_yiq_escalar(entrada):
    global imagen1yiq
    numero = float(entrada.get())
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    res_Y =(im1_Y * numero)
    plt.figure(figsize=(10, 5))
    plt.subplot(121)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y,im1_I,im1_Q))))
    plt.title("producto por escalar ")
    plt.subplot(122)
    plt.imshow(imagen1yiq)
    plt.title("imagen yiq original")
    plt.tight_layout()
    plt.show()
def division_imagenesyiq():
    global imagen1yiq, imagen2yiq
    im1_Y,im1_I,im1_Q =[imagen1yiq[:,:,i]for i in range (3)]
    im2_Y,im2_I,im2_Q =[imagen2yiq[:,:,i]for i in range (3)]
    res_Y = (im1_Y / im2_Y)
    res_I = (im1_Y * im1_I + im2_Y * im2_I) / (im1_Y + im2_Y)
    res_Q = (im1_Y * im1_Q + im2_Y * im2_Q) / (im1_Y + im2_Y)
    plt.figure(figsize=(12, 6))
    plt.subplot(131)
    plt.imshow(yiq_a_rgb(np.dstack((res_Y, res_I, res_Q))))
    plt.title("producto")
    plt.subplot(132)
    plt.imshow(imagen1yiq)
    plt.title("imagen 1 yiq")
    plt.subplot(133)
    plt.imshow(imagen2yiq)
    plt.title("imagen 2 yiq")
    plt.tight_layout()
    plt.show()


def ventana_2():
    ventana2 = tk.Toplevel(ventana)
    ventana2.title("Lighter y darker")
    boton_1 = tk.Button(ventana2, text="ifLighterRGB", command=ifLighterRGB)
    boton_2 = tk.Button(ventana2, text="ifDarkerRGB", command=ifDarkerRGB)
    boton_3 = tk.Button(ventana2, text="ifLighterYIQ", command=ifLighterYIQ)
    boton_4 = tk.Button(ventana2, text="ifDarkerRGB", command=ifDarkerYIQ)
    boton_1.pack()
    boton_2.pack()
    boton_3.pack()
    boton_4.pack()
    ventana2.mainloop()
def ventana_3():
    ventana3 = tk.Toplevel(ventana)
    ventana3.title("operaciones YIQ")
   
    boton_1 = tk.Button(ventana3, text="suma clampeada", command=suma_clampyiq)
    boton_2 = tk.Button(ventana3, text="resta clampeada", command=resta_clampyiq)
    boton_3 = tk.Button(ventana3, text="resta clampeada absoluto", command=resta_clampyiq_abs)
    boton_4 = tk.Button(ventana3, text="suma promedio", command=suma_promiyq)
    boton_5 = tk.Button(ventana3, text="resta promedio", command=resta_promyiq)
    boton_6 = tk.Button(ventana3, text="resta promedio absoluto", command=resta_promyiq_abs)
    boton_7 = tk.Button(ventana3, text="multiplicacion", command=multiplicacion_yiq)
    etiqueta = tk.Label(ventana3, text=" número:")
    etiqueta.pack()
    entrada_numero = tk.Entry(ventana3)
    entrada_numero.pack()
    boton_8 = tk.Button(ventana3, text="multiplicacion escalar",  command=lambda:multiplicacion_yiq_escalar(entrada_numero))
    boton_9 = tk.Button(ventana3, text="division", command=division_imagenesyiq)
    boton_1.pack()
    boton_2.pack()
    boton_3.pack()
    boton_4.pack()
    boton_5.pack()
    boton_6.pack()
    boton_7.pack()
    boton_8.pack()
    boton_9.pack()
   
    
    ventana3.mainloop()
def ventana_4():
    ventana4 = tk.Toplevel(ventana)
    ventana4.title("Lighter y darker")
    boton_1 = tk.Button(ventana4, text="suma ", command=suma_imagenes)
    boton_2 = tk.Button(ventana4, text="resta ", command=resta_imagenes)
    boton_3 = tk.Button(ventana4, text="suma promediada", command=suma_imagenespro)
    boton_4 = tk.Button(ventana4, text="resta promediada", command=resta_imagenespro)
    boton_5 = tk.Button(ventana4, text="producto", command=multiplicacion_imagenes)
    boton_6 = tk.Button(ventana4, text="division", command=div_rgb)
    boton_1.pack()
    boton_2.pack()
    boton_3.pack()
    boton_4.pack()
    boton_5.pack()
    boton_6.pack()
    ventana4.mainloop()



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

# Botones para realizar operaciones

boton_ventana2 = tk.Button(ventana, text="Lighter Y Darker", command=ventana_2)
boton_ventana3 = tk.Button(ventana, text="Operaciones YIQ", command=ventana_3)
boton_ventana4 = tk.Button(ventana, text="Operaciones RGB", command=ventana_4)


boton_ventana2.pack()
boton_ventana3.pack()
boton_ventana4.pack()
#yiq


   

ventana.mainloop()