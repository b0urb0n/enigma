import pytest

from enigma import reflector


@pytest.mark.xfail
def test_class():
    r = reflector.Reflector()


@pytest.mark.xfail
def test_encode():
	r = reflector.Reflector()
