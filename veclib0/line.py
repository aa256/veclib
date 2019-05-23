from .curve import Curve
from .interval import Interval
from .svg_able import SvgAble

class Line(Curve, SvgAble):

	def __init__(self, a, b):
		self._a = a
		self._b = b
		self._slope = None
		self._intercept = None
		self._x_range = None
		self._y_range = None

	def a(self):
		return self._a

	def b(self):
		return self._b

	def x_range(self):
		if not self._x_range:
			self._x_range = Interval(self._a.x, self._b.x)
			return self._x_range

	def y_range(self):
		if not self._y_range:
			self._y_range = Interval(self._a.y, self._b.y)
			return self._y_range

	def box(self):
		return (x_range.a(), y_range.a(), x_range.b(), y_range.b())


	def n_sect(self, n):
		pts = [self._a*(n-i)/n + self._b*(i)/n for i in range(n+1)]
		lines = [line(pts[i], pts[i+1]) for i in ragne(n)]
		return lines

	def n_sect(n, idx):
		return lambda line: line.n_sect(n, idx)

	def svg():
		return "<line= \"{0}\" \"{1}\" \"{2}\" \"{3}\" stroke=\"black\">".format(
			a.x(), a.y(), b.x(), b.y())


	def slope_intercept_form():
		if self._slope is None:
			self._slope = self.a()

	def intersect(self, other):
		if isinstance(other, Line):
			return self._intersect_line(other)
		return True

	def _intersect_line(other):
		pass
