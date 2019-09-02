from . import svg_tools

from .line import Line
from .svgable import Svgable
from .txable import Txable

class Polyline(Svgable, Txable):

	svg_prefix = "<polyline "
	svg_suffix = "/>"

	def __init__(self, pts, svg_params=None):
		if svg_params is None:
			svg_params = svg_tools.defaults
		self.pts = tuple(pts)
		self._lines = None
		Svgable.__init__(self, svg_params)

	def transform(self, txfn):
		return Polyline( [txfn*pt for pt in self.pts] )

	def lines(self):
		if not self._lines:
			self._lines = (Line(self.pts[i], self.pts[i+1]) for i in range(len(self.pts)-1))
		return self._lines

	def svg(self):
		print([str(pt) for pt in self.pts])
		out = Polyline.svg_prefix
		out += svg_tools.pts_as_pairs(*self.pts)
		out += svg_tools.svg_params(self.svg_params)
		out += Polyline.svg_suffix
		return out
