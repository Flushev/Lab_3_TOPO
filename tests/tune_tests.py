import pytest


class TestTune:

    def test_tune_create(self):
        tune = Tune(
            name='test_tune',
            path='tunes/test_tune.mp3'
        )
        assert tune is not None
