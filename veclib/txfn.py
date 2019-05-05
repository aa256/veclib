import vec
import mtx

class TxFn:

  def __init__(self, vec=vec.Z, mtx=mtx.I, rnf=True):
    self.mtx = mtx
    self.vec = vec
    self.is_rnf = rnf

  def rnf():
  	if self.is_rnf :
  		return self
  	return TxFn(mtx, ~mtx*vec, True)

  def lnf():
  	if not self.is_rnf:
  		return self
  	return TxFn(mtx, ~mtx*vec, False)

  def __mul__(self, txfn, lnf=False):
  	"""Eager multiplication."""
  	if (self.rnf or txfn.rnf):
  		if(not self.rnf):
  			self = self.rnf()
  		if(not txfn.rnf):
  			txfn = txfn.rnf()
  		return TxFn(self.vec + self.mtx*txfn.vec, self.mtx*txfn.mtx)
  	return TxFn(~txfn.mtx*self.vec + txfn.vec, self.mtx*txfn.mtx)

  def __inv__(self):
  	"""~inv operator"""
  	return TxFn(~self.mtx, -self.vec, not self.rnf)