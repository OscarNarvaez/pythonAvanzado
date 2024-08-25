import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

class Quiz:
    def __init__(self, root):
        self.root = root
        self.container_images = self.load_container_images()
        self.current_question = 0

        # Lista de imágenes de basuras y sus respuestas correctas
        self.questions = [
            {"correct": "plastico"},
            {"correct": "comida"},
            {"correct": "desperdicios"}
        ]
        self.trash_images = [
            "imagenes/basuras/bolsa_plastico.png",
            "imagenes/basuras/botella_plastico.png",
            "imagenes/basuras/botella_vidrio.png",
            "imagenes/basuras/carton_papel.png",
            "imagenes/basuras/espejo_vidrio.jpg",
            "imagenes/basuras/papel_papel.png",
        ]

    def load_container_images(self):
        # Cargar y redimensionar imágenes de los contenedores
        container1_img = Image.open("imagenes/contenedores/contenedor_plastico.png").resize((100, 100))
        container2_img = Image.open("imagenes/contenedores/contenedor_organico.png").resize((100, 100))
        container3_img = Image.open("imagenes/contenedores/contenedor_otros.png").resize((100, 100))
        return {
            "plastico": ImageTk.PhotoImage(container1_img),
            "comida": ImageTk.PhotoImage(container2_img),
            "desperdicios": ImageTk.PhotoImage(container3_img)
        }

    def start(self):
        self.show_question()

    def show_question(self):
        # Seleccionar una imagen de basura aleatoriamente
        trash_image_path = random.choice(self.trash_images)
        correct_answer = self.get_correct_answer(trash_image_path)

        # Mostrar la imagen de la basura
        trash_image = Image.open(trash_image_path).resize((100, 100))
        trash_photo = ImageTk.PhotoImage(trash_image)
        trash_label = tk.Label(self.root, image=trash_photo)
        trash_label.image = trash_photo
        trash_label.pack(pady=20)

        # Botones de los contenedores
        container1_button = tk.Button(self.root, image=self.container_images["plastico"],
                                      command=lambda: self.check_answer("plastico", correct_answer))
        container1_button.pack(side=tk.LEFT, padx=5)

        container2_button = tk.Button(self.root, image=self.container_images["comida"],
                                      command=lambda: self.check_answer("comida", correct_answer))
        container2_button.pack(side=tk.LEFT, padx=5)

        container3_button = tk.Button(self.root, image=self.container_images["desperdicios"],
                                      command=lambda: self.check_answer("desperdicios", correct_answer))
        container3_button.pack(side=tk.LEFT, padx=5)

    def get_correct_answer(self, image_path):
        # Obtener la respuesta correcta basada en la imagen de basura
        if "plastico" in image_path:
            return "plastico"
        elif "comida" in image_path:
            return "comida"
        elif "desperdicios" in image_path:
            return "desperdicios"

    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            messagebox.showinfo("Correcto", "¡Buena elección!")
        else:
            messagebox.showerror("Incorrecto", f"Este producto no debe ir en el contenedor de {answer}. Intenta de nuevo.")
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.show_question()
        else:
            messagebox.showinfo("Quiz Finalizado", "¡Has completado el quiz de reciclaje!")
