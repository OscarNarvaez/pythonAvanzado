import threading
from moviepy.editor import VideoFileClip

class VideoPlayer:
    def __init__(self, root, video_path, on_finish):
        self.root = root
        self.video_path = video_path
        self.on_finish = on_finish

    def play_video(self):
        # Reproducir el video en un hilo separado
        self.root.attributes('-fullscreen', True) # Pantalla completa al reproducir el video
        video_thread = threading.Thread(target=self._play)
        video_thread.start()

    def _play(self):
        clip = VideoFileClip(self.video_path)
        clip.preview()
        clip.close()  # Cerrar el video al finalizar
        self.on_finish()  # Llamar a la función cuando el video termine
