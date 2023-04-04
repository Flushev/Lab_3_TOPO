from classes.tune import Tune
import datetime
import schedule
from multiprocessing import *
import time


class Alarm:
    name: str
    description: str
    tune: Tune
    time: datetime.time
    is_active: bool
    process: Process = None

    def aside(self):
        time = datetime.time(hour=self.time.hour, minute=self.time.minute + 5)
        self.time = time

    def activate(self):
        print(f"\nСработал будильник {self.name}")
        mixer = self.tune.play()
        return mixer

    def start_process(self):
        self.process = Process(target=self.start_schedule, args=())
        self.process.start()

    def start_schedule(self):
        schedule.every().day.at("12:04").do(self.activate)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def __init__(self, name, description, tune, time, is_active=False):
        self.name = name
        self.description = description
        self.time = time
        self.tune = tune
        self.is_active = is_active
