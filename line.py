from .atom import Atom
from .vec import Vec

class Line(Atom):
	def __init__(self, a: Vec, b: Vec):
		self._a = a
		self._b = b

	def vecs():
		return [self.a, self.b]

	def params():
		return dict()

	def n_sect(self, n):
		pts = [self.a*((n-i)/n) + self.b*(i/n) for i in range(n+1)]
		return [Line(pts[i], pts[i+1]) for i in range(n)]