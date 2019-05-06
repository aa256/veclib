from .curve import Curve
class Line(Curve):

	def __init__(self, a, b):
		self._a = a
		self._b = b

	def n_sect(self, n, idx):
		pass

def n_sect(n, idx):
	return lambda line: line.n_sect(n, idx)