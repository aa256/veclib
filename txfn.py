from .txable import Txable
from .vec import Vec

class Txfn:
	"""
	Transformations read in order of right to left.
	"""
	def __init__(self, postshift=None, mat=None, preshift=None):
		self.pre = pre
		self.mat = mat
		self.post = post

	def __mul__(self, other):
		if isinstance(other, Vec):
			return post + mat*(pre + other)
		elif isinstance(other, Txable):
			return other.transform(self)
		elif isinstance(other, Txfn):
			new_post = self.post + self.mat*(self.pre + other.post)
			return Txfn(new_post, self.mat*other.mat, other.pre)


