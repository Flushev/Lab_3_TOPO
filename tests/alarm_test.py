import datetime

from classes.tune import Tune


class AlarmTest:
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
