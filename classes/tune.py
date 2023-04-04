import os
import pygame


class Tune:
    name: str
    path: str

    def check_exist(self):
        return os.path.isfile(self.path)

    def play(self):
        mixer = pygame.mixer
        mixer.init()
        mixer.music.load(self.path)
        mixer.music.play()
        return mixer

    def __init__(self, name, path):
        self.name = name
        self.path = path
