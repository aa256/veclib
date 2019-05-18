from .line import Line
from .vec import Vec
from . import stringtools

class Polyline:

	_svg_prefix = "<polyline points="
	_svg_suffix = ">"

	def __init__(self, *pts):
		n = len(pts)
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


	def svg(self):
		out = _svg_prefix
		out += stringtools.list_of_points(self._pts)
		out += " stroke=black stroke-width=3"
		out += _svg_suffix
		return out