from .svgable import Svgable
from .txable import Txable
from .vec import Vec

class Line(Svgable, Txable):
	def __init__(self, a: Vec, b: Vec, svg_params: dict=None) -> None:
		self.a = a
		self.b = b
		Svgable.__init__(self, svg_params)

	def vecs():
		return [self.a, self.b]

	def params():
		return dict()

	def n_sect(self, n):
		pts = [self.a*((n-i)/n) + self.b*(i/n) for i in range(n+1)]
		return [Line(pts[i], pts[i+1]) for i in range(n)]

	def transform(self, txfn):
		return Line(txfn*self.a, txfn*self.b)