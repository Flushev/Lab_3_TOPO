from .alarm import Alarm


class App:
    alarms: list[Alarm] | None

    def add_alarm(self, alarm: Alarm):
        if self.alarms is None:
            self.alarms = [alarm]
        else:
            self.alarms.append(alarm)

    def __init__(self, alarms=None):
        self.alarms = alarms