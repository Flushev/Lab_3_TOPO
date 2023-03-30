from .alarm import Alarm


class App:
    alarms: list[Alarm] | None

    def __init__(self, alarms=None):
        self.alarms = alarms