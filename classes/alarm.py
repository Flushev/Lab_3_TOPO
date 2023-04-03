from classes.tune import Tune
import datetime


class Alarm:
    name: str
    description: str
    tune: Tune
    time: datetime.time
    is_active: bool

    def aside(self):
        time = datetime.time(hour=self.time.hour, minute=self.time.minute + 5)
        self.time = time

    async def activate(self):
        return self.tune.play()

    def __init__(self, name, description, tune, time, is_active=False):
        self.name = name
        self.description = description
        self.time = time
        self.tune = tune
        self.is_active = is_active
