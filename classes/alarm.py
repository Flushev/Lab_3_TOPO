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
        time.sleep(2)
        return mixer

    def start_process(self):
        self.process = Process(target=self.start_schedule, args=())
        self.process.start()

    def start_schedule(self):
        hours = self.time.hour
        if hours < 10:
            hours = f'0{hours}'
        mins = self.time.minute
        if mins < 10:
            mins = f'0{mins}'

        schedule.every().day.at(f"{hours}:{mins}").do(self.activate)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def __init__(self, name, description, tune, time, is_active=False):
        self.name = name
        self.description = description
        self.time = time
        self.tune = tune
        self.is_active = is_active
