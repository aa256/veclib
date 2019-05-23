from .line import Line
from .svg_able import SvgAble
from .vec import Vec
from . import stringtools

import math

class Polyline(SvgAble):

	_svg_prefix = "<polyline points="
	_svg_suffix = "/>"

	def __init__(self, *pts):
		n = len(pts)
		print("SDFJSFD")
		print(n)
		if n < 3:
			return ValueError("Require at least 3 lines")
		self._pts = list(pts)

	def from_coords_list(*coords):
		n = len(coords)
		if n % 2 == 1:
			raise ValueError("Should specify an even number of coords")
		pts = []
		for i in range(n/2):
			pts.append()

	def lines(self):
		for i in range(len(self._pts)-1):
			a, b = self._pts[i], self._pts[i+1]

	def xvals(self):
		return list(pt.x for pt in self._pts)

	def yvals(self):
		return list(pt.y for pt in self._pts)

	def svg(self):
		out = self._svg_prefix
		out += stringtools.list_of_points(self._pts)
		out += " stroke=black stroke-width=3"
		out += self._svg_suffix
		return out

	def x_range(self):
		xvals = self.xvals()
		return Interval(min(xvals), max(xvals))

	def y_range(self):
		yvals = self.yvals()
		return Interval(min(yvals), max(yvals))	

	def box(self):
		xvals = self.xvals()
		yvals = self.yvals()
		return (min(xvals), min(yvals), max(xvals), max(yvals))


