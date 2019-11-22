import pytest

from enigma import rotor


def test_rotor_step(rotor_I):
	assert rotor_I._table == list(rotor.I)
	rotor_I._step()  # step once - r[0] should now be equal to orig[1]
	assert rotor_I._table[0] == rotor.I[1]
	rotor_I._step(25)  # step 25 times - r should now be equal to original table
	assert rotor_I._table == list(rotor.I)


def test_rotor_callback(rotor_I):
	flag = False
	def notch_cb():
		flag = True

	rotor_I._step(notch_callback=notch_cb)
	assert flag == False
	rotor_I._step(notch_callback=notch_cb)
	assert flag == True
