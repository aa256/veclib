from .vec import Vec
from .mtx import Mtx

class TxFn:

  def __init__(self, mtx=None, vec=None):
    self.mtx = mtx
    self.vec = vec

  def transform(self, vecs):
    for vec in vecs:

