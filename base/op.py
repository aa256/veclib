import typing

from .mat import Mat
from .vec import Vec

class Op:

	def __init__(self, val:typing.Union(Mat, Vec, Op)):
		if isinstance(val, Op):
			self = val
		else:
			self.val = val

	def __mul__(self, vec):
		if isinstance(self.val, Vec):
			return self.val + self.vec
		elif isinstance(self.val, Mat):
			return self.val*vec
		return ValueError("Unexpected operator value: {}\n".format(self.val))

	def is_vec(self):
		return isinstance(self.val, Vec)

	def is_mat(self):
		return isinstance(self.val, Mat)

	def swap(self, other):
		if self.is_vec() and other.is_vec():
			return (Op(self.val+other.val))
		elif self.is_mat() and other.is_mat():
			return (Op(self.val*other.val))
		elif self.is_mat() and other.is_vec():
			return (Op(self.val*other.val), self)
		elif self.is_vec() and other.is_mat():
			return (other, Op(~other.val*self.val))
		return ValueError("This shouldn't happen")

		