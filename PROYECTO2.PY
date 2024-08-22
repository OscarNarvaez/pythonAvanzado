import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Función para verificar la respuesta
def verificar_respuesta(tipo_contenedor):
    if tipo_contenedor == respuestas[imagen_actual]:
        messagebox.showinfo("Correcto", "¡Correcto! Este residuo va en el contenedor de " + tipo_contenedor)
    else:
        messagebox.showinfo("Incorrecto", "Incorrecto. Este residuo debe ir en el contenedor de " + respuestas[imagen_actual])
    siguiente_imagen()

# Función para mostrar la siguiente imagen
def siguiente_imagen():
    global imagen_actual, img_label
    imagen_actual = random.randint(0, len(imagenes) - 1)
    img = Image.open(imagenes[imagen_actual])
    img = img.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    img_label.config(image=img)
    img_label.image = img

# Configuración inicial de la ventana
root = tk.Tk()
root.title("Reciclaje para Niños")

# Lista de imágenes y respuestas correctas
imagenes = ["imagenes/carton.jpg", "imagenes/plastico.jpg", "imagenes/papel.jpg", "imagenes/vidrio.jpg"]
respuestas = ["papel", "plastico", "vidrio", "vidrio"]

imagen_actual = random.randint(0, len(imagenes) - 1)

# Mostrar la primera imagen
img = Image.open(imagenes[imagen_actual])
img = img.resize((200, 200), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
img_label = tk.Label(root, image=img)
img_label.grid(row=0, column=0, columnspan=3)

# Botones de los contenedores
btn_papel = tk.Button(root, text="Papel", command=lambda: verificar_respuesta("papel"))
btn_papel.grid(row=1, column=0)

btn_plastico = tk.Button(root, text="Plástico", command=lambda: verificar_respuesta("plastico"))
btn_plastico.grid(row=1, column=1)

btn_vidrio = tk.Button(root, text="Vidrio", command=lambda: verificar_respuesta("vidrio"))
btn_vidrio.grid(row=1, column=2)

root.mainloop()