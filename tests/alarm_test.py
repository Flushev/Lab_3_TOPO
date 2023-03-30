import datetime

import pytest

from classes.tune import Tune
from classes.alarm import Alarm


class TestAlarm:
    @staticmethod
    def create_tune():
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.mp3'
        )
        return tune

    def test_alarm_create(self):
        tune = self.create_tune()
        time = datetime.time(hour=8, minute=0)

        alarm = Alarm(
            name='test_alarm',
            description='test_description',
            tune=tune,
            time=time
        )
        assert alarm is not None

    def test_alarm_aside(self):
        tune = self.create_tune()
        time = datetime.time(hour=8, minute=0)
        alarm = Alarm(
            name='test_alarm',
            description='test_description',
            tune=tune,
            time=time
        )
        time_1 = alarm.time.minute
        alarm.aside()
        time_2 = alarm.time.minute
        assert time_2 == time_1 + 5

