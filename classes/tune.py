import os


class Tune:
    name: str
    path: str

    def check_exist(self):
        return os.path.isfile(self.path)

    def __init__(self, name, path):
        self.name = name
        self.path = path
