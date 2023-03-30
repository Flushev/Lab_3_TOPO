from classes.tune import Tune
import datetime


class Alarm:
    name: str
    description: str
    tune: Tune
    time: datetime.time

    def __init__(self, name, description, tune, time):
        self.name = name
        self.description = description
        self.time = time
        self.tune = tune
