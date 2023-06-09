import datetime

import pytest

from classes.tune import Tune
from classes.alarm import Alarm


class TestAlarm:
    @staticmethod
    def create_tune():
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.wav'
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

    def test_alarm_activate(self):
        tune = self.create_tune()
        time = datetime.time(hour=8, minute=0)
        alarm = Alarm(
            name='test_alarm',
            description='test_description',
            tune=tune,
            time=time
        )
        mixer = alarm.activate()
        assert mixer is not None

    def test_alarm_start_process(self):
        tune = self.create_tune()
        time = datetime.time(hour=8, minute=0)
        alarm = Alarm(
            name='test_alarm',
            description='test_description',
            tune=tune,
            time=time
        )
        alarm.start_process()
        assert alarm.process is not None

