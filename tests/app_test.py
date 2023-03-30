from classes.app import App
from classes.tune import Tune
from classes.alarm import Alarm
import datetime


class TestApp:
    @staticmethod
    def create_tune():
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.mp3'
        )
        return tune

    @staticmethod
    def create_alarm(self):
        tune = self.create_tune()
        time = datetime.time(hour=8, minute=0)

        alarm = Alarm(
            name='test_alarm',
            description='test_description',
            tune=tune,
            time=time
        )
        return alarm

    def test_create_app(self):
        app = App()
        assert app is not None

    def test_app_add_alarm(self):
        app = App()
        alarm = self.create_alarm(self)
        app.add_alarm(alarm)
        alarms = app.alarms
        assert alarms is not None

    def test_app_get_alarm_list(self):
        app = App()
        alarm = self.create_alarm(self)
        app.add_alarm(alarm)
        res = app.get_alarm_list()
        assert res
