import os
import pygame


class Tune:
    name: str
    path: str

    def check_exist(self):
        return os.path.isfile(self.path)

    async def play(self):
        mixer = pygame.mixer
        mixer.music.load(self.path)
        mixer.music.play(-1)
        return mixer

    def __init__(self, name, path):
        self.name = name
        self.path = path
