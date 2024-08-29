import tkinter as tk
from video_player import VideoPlayer
from quiz import Quiz
import os

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Concientización Ambiental para Niños")
        self.root.geometry("800x600")

        # Ruta absoluta del video
        video_path = os.path.join(os.path.dirname(__file__), "video", "reciclajeTutorial.mp4")

        # Iniciar la reproducción del video
        self.video_player = VideoPlayer(self.root, video_path, self.show_quiz_button)
        self.video_player.play_video()

    def show_quiz_button(self):
        # Mostrar botón "Siguiente" al finalizar el video
        next_button = tk.Button(self.root, text="Siguiente", font=("Arial", 20), command=self.start_quiz)
        next_button.pack(expand=True)

    def start_quiz(self):
        # Limpiar la ventana principal antes de iniciar el quiz
        for widget in self.root.winfo_children():
            widget.destroy()

        # Iniciar el quiz
        quiz = Quiz(self.root)
        quiz.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()