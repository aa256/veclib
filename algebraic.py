import numbers
import typing


class RingElem:
	def __init__(self):
		pass

	def __add__(self, other):
		if other == 0:
			return self

	def __neg__(self):
		pass

	def __mul__(self, other):
		if other == 1:
			return self

	@classmethod
	def from_real(cls, x:numbers.Real):
		pass


class FieldElem(RingElem):
	def __truediv__(self, other):
		pass


RingType = typing.NewType('RingType', typing.Union[numbers.Number, RingElem])
FieldType = typing.NewType(
	'FieldType', typing.Union[numbers.Number, FieldElem])
