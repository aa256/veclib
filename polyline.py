import math

from .atom import Atom
from .line import Line

class Polyline(Atom):

	svg_prefix = "<polyline "
	svg_suffix = "/>"

	def __init__(self, pts):
		self.pts = tuple(pts)
		self._lines = None

	def vecs(self):
		return self.pts

	def params(self):
		return dict()

	def lines(self):
		if not self._lines:
			self._lines = (Line(self.pts[i], self.pts[i+1]) for i in xrange(len(self.pts-1)))
		return self._lines


