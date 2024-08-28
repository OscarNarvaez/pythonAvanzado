import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class Quiz:
    def __init__(self, root):
        self.root = root
        self.container_images = self.load_container_images()
        
        self.root.configure(bg="#ADD8E6")

        # Lista de imágenes de basuras y sus respuestas correctas
        self.trash_images = [
            {"path": "imagenes/basuras/bolsa_plastico.png", "correct": "plastico"},
            {"path": "imagenes/basuras/botella_plastico.png", "correct": "plastico"},
            {"path": "imagenes/basuras/botella_vidrio.png", "correct": "otros"},
            {"path": "imagenes/basuras/carton_papel.png", "correct": "comida"},
            {"path": "imagenes/basuras/espejo_vidrio.jpg", "correct": "otros"},
            {"path": "imagenes/basuras/papel_papel.png", "correct": "comida"},
        ]

        # Cargar la primera pregunta
        self.show_question()

    def load_container_images(self):
        # Cargar y redimensionar imágenes de los contenedores
        container1_img = Image.open("imagenes/contenedores/contenedor_plastico.png").resize((200, 150))  # Contenedor de plástico
        container2_img = Image.open("imagenes/contenedores/contenedor_organico.png").resize((200, 150))  # Contenedor de comida
        container3_img = Image.open("imagenes/contenedores/contenedor_otros.png").resize((200, 150))  # Contenedor de desperdicios
        return {
            "plastico": ImageTk.PhotoImage(container1_img),
            "comida": ImageTk.PhotoImage(container2_img),
            "otros": ImageTk.PhotoImage(container3_img)
        }

    def show_question(self):
        # Limpiar la pantalla de la imagen de basura anterior
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Label):
                widget.destroy()

        # Seleccionar una imagen de basura aleatoriamente
        question = random.choice(self.trash_images)
        trash_image_path = question["path"]
        correct_answer = question["correct"]

        # Mostrar la imagen de la basura
        trash_image = Image.open(trash_image_path).resize((300, 250))
        trash_photo = ImageTk.PhotoImage(trash_image)
        trash_label = tk.Label(self.root, image=trash_photo)
        trash_label.image = trash_photo
        trash_label.pack(pady=50)

        # Botones de los contenedores (Fijos en la pantalla)
        container1_button = tk.Button(self.root, image=self.container_images["plastico"],
                                      command=lambda: self.check_answer("plastico", correct_answer))
        container1_button.place(x=100, y=400)  # Posicionamiento fijo

        container2_button = tk.Button(self.root, image=self.container_images["comida"],
                                      command=lambda: self.check_answer("comida", correct_answer))
        container2_button.place(x=300, y=400)  # Posicionamiento fijo

        container3_button = tk.Button(self.root, image=self.container_images["otros"],
                                      command=lambda: self.check_answer("otros", correct_answer))
        container3_button.place(x=500, y=400)  # Posicionamiento fijo

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            messagebox.showinfo("Muy Bien", "¡Buena elección!")
        else:
            messagebox.showerror("Incorrecto", f"Este producto no debe ir en el contenedor de {answer}. Intenta de nuevo.")
        
        self.show_question()