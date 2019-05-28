import math

from . import svg_tools

from .line import Line
from .txable import Txable

class Polyline(Txable):

	svg_prefix = "<polyline "
	svg_suffix = "/>"

	def __init__(self, pts, params=None):
		if params is None:
			params = svg_tools.defaults
		self.pts = tuple(pts)
		self._lines = None

	def transform(self, txfn):
		return Polyline([txfn*self.pts[i] for i in range(len(self.pts))], self.params)

	def lines(self):
		if not self._lines:
			self._lines = (Line(self.pts[i], self.pts[i+1]) for i in xrange(len(self.pts-1)))
		return self._lines

	def svg(self):
		out = svg_prefix
		out += svg_tools.svg_points(self.pts)
		out += svg_tools.svg_params(self.params)
		out += svg_suffix