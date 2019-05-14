from .curve import Curve
class Line(Curve):

	def __init__(self, a, b):
		self._a = a
		self._b = b
		self._slope = None
		self._intercept = None

	def a(self):
		return self._a

	def b(self):
		return self._b

	def n_sect(self, n, idx):
		pass

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

