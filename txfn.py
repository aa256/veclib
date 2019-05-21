import math

from .vec import Vec, Z
from .mtx import Mtx, I

class Txfn:

	def __init__(self, vec=Z, mtx=I, rnf=True):
		self.mtx = mtx
		self.vec = vec
		self.is_rnf = rnf

	def rnf():
		"""
		
		"""
		if self.is_rnf:
			return self
		return Txfn(mtx, ~mtx*vec, True)

	def lnf():
		if not self.is_rnf:
			return self
		return Txfn(mtx, ~mtx*vec, False)

	def __mul__(self, Txfn, lnf=False):
		"""Eager multiplication."""
		if (self.rnf or Txfn.rnf):
			if(not self.rnf):
				self = self.rnf()
			if(not Txfn.rnf):
				Txfn = Txfn.rnf()
			return Txfn(self.vec + self.mtx*Txfn.vec, self.mtx*Txfn.mtx)
		return Txfn(~Txfn.mtx*self.vec + Txfn.vec, self.mtx*Txfn.mtx)

	def __inv__(self):
		"""~inv operator"""
		return Txfn(~self.mtx, -self.vec, not self.rnf)

	@classmethod
	def rotate_Txfn(n):
		phi = 2*math.pi/n
		return Txfn(mtx=Mtx(math.cos(phi), -math.sin(phi), math.sin(phi), math.cos(phi)))