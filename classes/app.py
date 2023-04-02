from .alarm import Alarm
from .tune import Tune


class App:
    alarms: list[Alarm] | None = None
    tunes: list[Tune] | None = None

    def add_alarm(self, alarm: Alarm):
        if self.alarms is None:
            self.alarms = [alarm]
        else:
            self.alarms.append(alarm)

    def get_alarm_list(self):
        i = 1
        if self.alarms is not None:
            for alarm in self.alarms:
                print(f"{i}. {alarm.name}")
                i += 1
        else:
            print("Список будильников пуст")
        return True

    def get_tune_list(self):
        i = 1
        if self.tunes is not None:
            for tune in self.tunes:
                print(f"{i}. {tune.name}")
                i += 1
        else:
            print("Список рингтонов пуст")
        return True

    def __init__(self, alarms=None):
        self.alarms = alarms