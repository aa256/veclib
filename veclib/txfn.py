from .vec import Vec
from .mtx import Mtx

class TxFn:

  def __init__(self, vec=Vec.Z, mtx=Mtx.I, rnf=True):
    self.mtx = mtx
    self.vec = vec
    self.is_rnf = rnf

  def rnf():
  	if self.is_rnf :
  		return self
  	return TxFn(mtx, ~mtx*vec, True)

  def lnf():
  	if ! self.is_rnf:
  		return self
  	return TxFn(mtx, ~mtx*vec, False)

  def __mul__(self, txfn, lnf=False):
  	"""Eager multiplication."""
  	if (self.rnf || txfn.rnf):
  		if(! self.rnf):
  			self = self.rnf()
  		if(! txfn.rnf):
  			txfn = txfn.rnf()
  		return TxFn()



  def __matmul__(self, vec):
  	"""Lazy multiplication.

  	"""


  def __inv__(self):
  	"""~inv operator"""
  	return TxFn(~self.mtx, -self.vec, !self.rnf)