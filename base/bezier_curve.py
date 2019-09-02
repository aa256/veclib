from .polynom import Polynom
from .svgable import Svgable


class BezierCurve(Svgable, Txable):
	"""
	https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths#Curve_commands

	SVG only supports quadratic (line), cubic (C) and quartic Bezier curves.
	SVG: M - move to dx dy, L - lineTo, Z - close path.

	Curve - C x1 y1 x2 y2
	"""
	def __init__(self, pts, svg_params):
		self.pts = tuple(pts)

	def __mul__(self, txfn):
		return BezierCurve(txfn*pt for pt in self.pts)

	"Code for generating Bernstein polynomials. Not clear if needed. Should
	be put on the scrap heap."

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
