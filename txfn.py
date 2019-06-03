import math
import typing

from .mat import Mat, I
from .txable import Txable
from .vec import Vec, z


class Txfn:

	def __init__(self, *ops:typing.Union[Mat, Vec]):
		"""
		Transformations read in order of right to left.
		"""
		self.ops = tuple(ops)
		self.n = len(self.ops)

	def __invert__(self):
		return Txfn(
			-self.op[i] if isinstance(self.op[i], Vec)
			else ~self.op[i] for i in range(self.n-1,-1,-1))

	def __mul__(self, other):
		if isinstance(other, Vec):
			return self.__mulops(other)
		elif isinstance(other, Txable):
			return other.transform(self)
		elif isinstance(other, Txfn):
			return Txfn(*self.ops, *other.ops)

	def __mulops(self, vec, idx=self.n-1):
		op = self.ops[idx]
		if isinstance(op, Mat):
			out = op*vec
		if idx > 0:
			return self.__mulops(out, idx-1)
		return out

	@classmethod
	def rotate(cls, b, a=1, ctr=z):
		c = math.cos(2*math.pi*a/b)
		s = math.sin(2*math.pi*a/b)
		mat = Mat(c, -s, s, c)
		return Txfn(ctr, mat, -ctr)

	@classmethod
	def scale(cls, s, ctr=z):
		return Txfn(ctr, Mat(s, 0, 0, s), -ctr)