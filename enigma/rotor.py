from string import ascii_uppercase
from typing import AnyStr, Callable, Collection



# Commercial Enigma A, B - 1924
IC = 'DMTWSILRUYQNKFEJCAZBPGXOHV'
IIC = 'HQZGPJTMOBLNCIFDYAWVEUSRKX'
IIIC = 'UQNTLSZFMREHDPXKIBVYGJCWOA'

# German Railway (Rocket) - 7 February, 1941
I = 'JGDQOXUSCAMIFRVTPNEWKBLZYH'
II = 'NTZPSFBOKMWRCJDIVLAEYUXHGQ'
III = 'JVIUBHTCDYAKEQZPOSGXNRMWFL'
UKW = 'QYHOGNECVPUZTFDJAXWMKISRBL'
ETW = 'QWERTZUIOASDFGHJKPYXCVBNML'

# TODO - add more rotors


class Rotor(object):
	"""
	Enigma Rotor class represents a rotor/disk that would've been used in the Enigma Machine

	Wiring:
	Rotors had internal wiring that allowed letters to be "encoded" via pseudo-random electrical wiring
	The wiring is simulated with a list that is "rotated" via .insert() and .pop()

	Offset:
	Rotora were often offset to offer an additional layer of scrambling.  This is accomplished by calling
	.step(n) where n is the offset (int).

	Ring Setting:
	NOT IMPLEMENTED YET
	This is represented by a negative offset that changed the physical rotor by n
	"""
	def __init__(self, table: AnyStr, *, offset: int = 0, notches: Collection = ()):
		if len(table) != len(ascii_uppercase):
			raise ValueError(f"Rotor must contain {len(ascii_uppercase)} letters")

		self._table = list(table)
		self._notches = notches
		self._step(offset)

	def _step(self, count: int = 1, *, notch_callback: Callable = None):
		"""
		Advance the rotor n times and executes notch_callback if provided.  The callback should be the next rotor's
		.step() method.

		:param count: The number of times to advance the rotor
		:param notch_callback: The callback function to execute if the rotor is advanced while in the notched position
		"""
		for _ in range(count):
			self._table.insert(0, self._table.pop())
			if self._table[0] in self._notches and notch_callback:
				# notch_callback is usually the next rotor's .step() method
				notch_callback()

	def encode(self, letter: AnyStr, *, step: bool = True):
		"""
		Advances the rotor by one step and encodes the given letter.

		:param letter: The letter to encode
		:param step: Whether or not to advance the rotor
		"""
		if step:
			self._step()

		index = ascii_uppercase.index(letter.upper())
		return self._table[index]
