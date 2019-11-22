import pytest

from enigma import rotor


@pytest.fixture
def rotor_I():
	return rotor.Rotor(rotor.I, notches=('D'))
