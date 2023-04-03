import pytest

from classes.tune import Tune


class TestTune:

    def test_tune_create(self):
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.mp3'
        )
        assert tune is not None

    def test_tune_check_exist(self):
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.mp3'
        )
        assert tune is not None
        exist = tune.check_exist()
        assert exist is True or exist is False

    def test_tune_play(self):
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.mp3'
        )
        assert tune is not None
        mixer = tune.play()
        assert mixer is not None

