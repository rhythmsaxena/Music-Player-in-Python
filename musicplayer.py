import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Rhythm's Music Player")
        self.root.geometry("300x100")

        pygame.init()

        self.playlist = []
        self.current_track = 0

        self.load_button = tk.Button(root, text="Load Music", command=self.load_music)
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)

        self.load_button.pack(fill="x")
        self.play_button.pack(fill="x")
        self.stop_button.pack(fill="x")

    def load_music(self):
        directory = filedialog.askdirectory()
        os.chdir(directory)

        for song in os.listdir(directory):
            if song.endswith(".mp3"):
                self.playlist.append(song)

    def play_music(self):
        if len(self.playlist) == 0:
            return

        pygame.mixer.music.load(self.playlist[self.current_track])
        pygame.mixer.music.play()

    def stop_music(self):
        pygame.mixer.music.stop()

root = tk.Tk()
music_player = MusicPlayer(root)
root.mainloop()
