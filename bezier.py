from .polynom import Polynom
from .svgable import Svgable


class BezierCurve(Svgable):

	def __init__(self, pts, svg_params):
		self.pts = tuple(pts)
		self.a = pts[0]
		self.b = pts[-1]

	def __mul__(self, txfn):
		return BezierCurve(txfn*pt for pt in self.pts)

	bernstein_bases = [(1), (Polynom([1,-1]), Polynom([0,1]))]

	@classmethod
	def bernstein(cls, n, i=None):
		if len(cls.bernstein_bases) > n:
			if i is None:
				return cls.bernstein_bases[n]
			elif i < 0 or i > n:
				return 0
			return cls.bernstein_bases[n][i]

		b0, b1 = cls.bernstein(1, 0), cls.bernstein(1, 1)
		cls.bernstein_bases.append(
			[cls.berstein(n-1, i-1)*b0+cls.bernstein(n-1, i)*b1 for i in range(n-1)])
		return cls.bernstein(n, i)
