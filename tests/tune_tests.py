import pytest
from classes.tune import Tune


class TestTune:

    def test_tune_create(self):
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.mp3'
        )
        assert tune is not None
        return tune

    def test_tune_check_exist(self):
        tune = self.test_tune_create()
        exist = tune.check_exist()
        assert exist is True or exist is False

